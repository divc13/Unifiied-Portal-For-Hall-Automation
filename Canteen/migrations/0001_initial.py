# Generated by Django 4.1.6 on 2023-03-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('User_Name', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.TextField(max_length=30)),
                ('Amount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.TextField(max_length=50)),
                ('Price', models.PositiveIntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=20)),
                ('Name', models.TextField(max_length=30)),
                ('Item_Name', models.TextField(max_length=50)),
                ('Price', models.PositiveIntegerField(default=20)),
                ('Quantity', models.PositiveIntegerField(default=1)),
                ('Amount', models.PositiveIntegerField(default=20)),
                ('Order_Date_Time', models.DateTimeField()),
                ('Cart_Status', models.BooleanField(default=False)),
                ('Processing_Status', models.BooleanField(default=False)),
                ('Accepted_Status', models.BooleanField(default=False)),
                ('History_Status', models.BooleanField(default=False)),
                ('Served_Status', models.BooleanField(default=False)),
                ('Payment_Status', models.BooleanField(default=False)),
            ],
        ),
    ]
