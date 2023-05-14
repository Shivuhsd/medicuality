# Generated by Django 4.2 on 2023-05-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_patient_info_city_patient_info_patient_address_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment_info',
            old_name='billing_address',
            new_name='billing_address_1',
        ),
        migrations.AddField(
            model_name='payment_info',
            name='billing_address_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='payment_info',
            name='billing_address_city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='payment_info',
            name='billing_address_pin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='payment_info',
            name='billing_address_state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]