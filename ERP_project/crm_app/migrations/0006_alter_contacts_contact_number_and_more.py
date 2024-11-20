# Generated by Django 4.0.5 on 2024-10-11 06:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0005_contacts_leads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Contact number must be exactly 10 digits.', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email_id',
            field=models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')]),
        ),
        migrations.AlterField(
            model_name='leads',
            name='contact_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Contact number must be exactly 10 digits.', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='leads',
            name='email_id',
            field=models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')]),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')]),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='emp_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
