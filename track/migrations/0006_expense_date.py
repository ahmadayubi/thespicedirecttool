# Generated by Django 3.0.2 on 2020-01-23 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0005_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
