# Generated by Django 5.1.2 on 2024-11-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0034_merge_20241107_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeleave',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Created', max_length=10),
        ),
    ]