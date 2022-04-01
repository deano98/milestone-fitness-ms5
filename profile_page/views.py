from django.shortcuts import render
from membership.models import Member
from nutrition.models import MealType

# Create your views here.

def profile_page(request):
    ''' View to return the profile page page '''

    current_member = Member.objects.get(user=request.user)
    meal_types = MealType.objects.all()

    return render(request, 'profile_page/profile.html', {
        'current_member': current_member,
        'meal_types': meal_types,
    })
