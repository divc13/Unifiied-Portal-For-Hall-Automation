# Generated by Django 4.1.6 on 2023-03-13 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_Month', models.IntegerField(default=1)),
                ('Month_Name', models.TextField(default='January', max_length=9)),
                ('Total_Days', models.IntegerField(default=0)),
                ('rebate_days', models.IntegerField(default=0)),
                ('User_Name', models.CharField(max_length=20)),
                ('Basic_Amount', models.FloatField(default=0)),
                ('Extras_Amount', models.FloatField(default=0)),
                ('Mess_Bill', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Datewise_BDMR',
            fields=[
                ('Date', models.DateField(primary_key=True, serialize=False)),
                ('BDMR', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meal', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Breakfast', max_length=9)),
                ('Meal_Date', models.DateField(default=datetime.datetime.now)),
                ('Item_Name', models.CharField(max_length=50)),
                ('Price', models.IntegerField(default=20)),
                ('Start_Time', models.DateTimeField(default=datetime.datetime.now)),
                ('End_Time', models.DateTimeField(default=datetime.datetime.now)),
                ('Capacity', models.IntegerField(default=200)),
                ('Available_Orders', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meal', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Breakfast', max_length=9)),
                ('Order_Date_Time', models.DateTimeField()),
                ('Meal_Date', models.DateField()),
                ('User_Name', models.CharField(max_length=20)),
                ('Item_Name', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField(default=1)),
                ('Price', models.IntegerField(default=20)),
                ('Amount', models.IntegerField(default=20)),
                ('History_Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rating_Regular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meal', models.CharField(choices=[('Breakfast', 'B'), ('Lunch', 'L'), ('Dinner', 'D')], max_length=9)),
                ('Day', models.CharField(choices=[('Monday', 'Mon'), ('Tuesday', 'Tues'), ('Wednesday', 'Wed'), ('Thursday', 'Thu'), ('Friday', 'Fri'), ('Saturday', 'Sat'), ('Sunday', 'Sun')], max_length=9)),
                ('User_Name', models.CharField(max_length=20)),
                ('Rating_Value', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Rebate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_From', models.DateField()),
                ('Date_To', models.DateField()),
                ('Rebate_Days', models.IntegerField(default=0)),
                ('User_Name', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Regular_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(choices=[('Monday', 'Mon'), ('Tuesday', 'Tues'), ('Wednesday', 'Wed'), ('Thursday', 'Thu'), ('Friday', 'Fri'), ('Saturday', 'Sat'), ('Sunday', 'Sun')], default='Mon', max_length=9)),
                ('Meal', models.CharField(choices=[('Breakfast', 'B'), ('Lunch', 'L'), ('Dinner', 'D')], default='B', max_length=9)),
                ('Items', models.CharField(max_length=100)),
                ('Rating', models.FloatField(default=0.0)),
            ],
        ),
    ]
