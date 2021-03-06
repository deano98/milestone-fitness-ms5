from datetime import datetime as dt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import stripe
from .models import Member
from .forms import TdeeForm


def membership(request):
    ''' View to return the membership page '''
    if request.method == 'POST':
        tdee_data = request.POST
        gender = tdee_data.get("gender")
        weight = float(tdee_data.get("weight"))
        height = float(tdee_data.get("height"))
        age = float(tdee_data.get("age"))
        activity = tdee_data.get("activity")
        multiplier = 1

        if gender == "male":
            bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        else:
            bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

        if activity == "sedentary":
            multiplier = 1.2
        elif activity == "light":
            multiplier = 1.375
        elif activity == "moderate":
            multiplier = 1.55
        elif activity == "heavy":
            multiplier = 1.725
        else:
            multiplier = 1.9

        user_tdee = bmr * multiplier
        rounded_tdee = round(user_tdee/100)*100
        current_member = Member.objects.get(user=request.user)
        current_member.tdee = rounded_tdee
        current_member.gender = gender
        current_member.weight = weight
        current_member.current_weight = weight
        current_member.height = height
        current_member.age = age
        current_member.activity = activity
        current_member.tdee_update = dt.now()
        current_member.save()

        return redirect('profile_page:profile_page')

    return render(request, 'membership/membership.html', {
        'tdee_form': TdeeForm(),
    })


stripe.api_key = "sk_test_51KPpqoJAp5w3wtxOBWUnJsxJqEb3uaoG7AK0cbFTyHv5uYJsSYeLm5hb2e4CQ2HCO2sPKxaaNPBwuD9KK6KHqm5H0022pEx4RX"  # noqa


@login_required
def checkout(request):
    '''
    A view render the checkout page and
    generate a stripe checkout session
    when a user wants to subscribe to the site
    '''
    try:
        if request.user.member.membership:
            return redirect('settings')
    except Member.DoesNotExist:
        pass

    price = 0
    if request.method == 'POST':
        pass
    else:
        price = 20
        price_id = "price_1Kdfs8JAp5w3wtxO6l24lzML"

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            customer_email=request.user.email,
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://milestone-fitness.herokuapp.com/membership/success?session_id={CHECKOUT_SESSION_ID}',  # noqa
            cancel_url='https://milestone-fitness.herokuapp.com/membership/cancel',
        )

        return render(request, 'membership/checkout.html', {
            'session_id': session.id,
            'price': price,
            })


def success(request):
    ''' View to return success page after successfully purchasing a sub'''
    if request.method == 'GET' and 'session_id' in request.GET:
        session = stripe.checkout.Session.retrieve(request.GET['session_id'],)
        member = Member()
        member.user = request.user
        member.stripe_id = session.customer
        member.membership = True
        member.cancel_at_end = False
        member.stripe_member_id = session.subscription
        member.save()
    return render(request, 'membership/success.html')


def cancel(request):
    '''
    View to return an error page after
    an unsuccessful attempt tp buy a sub
    '''
    return render(request, 'membership/cancel.html')


@login_required
def settings_page(request):
    '''View to return the user settings page'''
    membership_bool = False
    cancel_at_end = False
    if request.method == 'POST':
        subscription = stripe.Subscription.retrieve(
            request.user.member.stripe_member_id
            )
        subscription.cancel_at_period_end = True
        request.user.member.cancel_at_end = True
        cancel_at_end = True
        subscription.save()
        request.user.member.save()
    else:
        try:
            if request.user.member.membership:
                membership_bool = True
            if request.user.member.cancel_at_end:
                cancel_at_end = True
        except Member.DoesNotExist:
            membership_bool = False

    return render(request, 'membership/settings.html', {
        'membership_bool': membership_bool,
        'cancel_at_end': cancel_at_end,
        })
