# Generated by Django 3.2 on 2022-03-30 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_member_tdee_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='tdee_update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
