# Generated by Django 2.2.6 on 2019-12-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receptionist', '0006_auto_20191218_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation_record',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('UnFit', 'Unfit'), ('Fit', 'Fit')], default='Pending', max_length=13),
        ),
    ]