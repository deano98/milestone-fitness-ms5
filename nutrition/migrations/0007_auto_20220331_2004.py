# Generated by Django 3.2 on 2022-03-31 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0006_meal'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='ingredient_1',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredient_2',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredient_3',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredient_4',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredient_5',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredient_6',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredient_7',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredient_8',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
