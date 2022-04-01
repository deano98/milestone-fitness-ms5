# Generated by Django 3.2 on 2022-03-31 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0004_auto_20220330_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='leanmince',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='leanturkey',
            name='calories',
        ),
        migrations.DeleteModel(
            name='AromaticTurkey',
        ),
        migrations.DeleteModel(
            name='Calories',
        ),
        migrations.DeleteModel(
            name='LeanMince',
        ),
        migrations.DeleteModel(
            name='LeanTurkey',
        ),
    ]
