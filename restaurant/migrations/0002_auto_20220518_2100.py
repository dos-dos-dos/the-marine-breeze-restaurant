# Generated by Django 3.2 on 2022-05-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslots',
            name='slot_hours',
        ),
        migrations.AlterField(
            model_name='openhours',
            name='week_day',
            field=models.CharField(choices=[('SUN', 'SUNDAY'), ('MON', 'MONDAY'), ('TUES', 'TUESDAY'), ('WED', 'WEDNESDAY'), ('THU', 'THURSDAY'), ('FRI', 'FRIDAY'), ('SAT', 'SATURDAY')], max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='timeslots',
            name='slot_end',
            field=models.TimeField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='timeslots',
            name='slot_start',
            field=models.TimeField(blank=True, unique=True),
        ),
    ]
