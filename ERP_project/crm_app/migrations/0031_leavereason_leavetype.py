# Generated by Django 5.1.2 on 2024-11-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0030_rename_verif_status_id_employeequalification_verify_status_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveReason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_reason', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_Type', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
