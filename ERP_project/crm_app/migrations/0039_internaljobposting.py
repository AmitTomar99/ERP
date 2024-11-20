# Generated by Django 5.1.2 on 2024-11-11 05:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0038_jobrequisition'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalJobPosting',
            fields=[
                ('applicationId', models.AutoField(primary_key=True, serialize=False)),
                ('applicationDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='Applied', max_length=20)),
                ('applyingPartyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applying_party', to='crm_app.hr_employee', to_field='employee_id')),
                ('approverPartyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approver_party', to='crm_app.hr_employee', to_field='employee_id')),
                ('jobRequisitionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.jobrequisition')),
            ],
        ),
    ]
