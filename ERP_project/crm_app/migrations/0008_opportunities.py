# Generated by Django 4.0.5 on 2024-10-11 06:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0007_alter_leads_contact_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opportunity_name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('sale_stage', models.CharField(max_length=255)),
                ('probability', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('description', models.TextField(blank=True, null=True)),
                ('expected_close_date', models.DateField()),
                ('lead_source', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_opportunities', to='crm_app.registeruser')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opportunities', to='crm_app.leads')),
            ],
        ),
    ]