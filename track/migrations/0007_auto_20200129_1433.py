# Generated by Django 3.0.2 on 2020-01-29 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0006_expense_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Zak', 'Zak'), ('Adil', 'Adil'), ('Yama', 'Yama')], default='yama', max_length=15)),
                ('order_id', models.CharField(max_length=100)),
                ('amount_paid', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.DeleteModel(
            name='Packager',
        ),
    ]
