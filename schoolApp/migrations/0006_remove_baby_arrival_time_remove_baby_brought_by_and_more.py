# Generated by Django 5.0.3 on 2024-05-20 19:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolApp', '0005_remove_baby_fee_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baby',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='baby',
            name='brought_by',
        ),
        migrations.RemoveField(
            model_name='baby',
            name='period_of_stay',
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brought_by', models.CharField(max_length=50)),
                ('period_of_stay', models.CharField(max_length=10)),
                ('fee_amount', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('Baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolApp.baby')),
            ],
        ),
    ]