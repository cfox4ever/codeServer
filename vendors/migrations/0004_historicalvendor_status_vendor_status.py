# Generated by Django 5.1.1 on 2024-12-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_alter_vendor_options_remove_historicalvendor_files_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvendor',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('on_hold', 'On Hold'), ('active', 'Active'), ('in-active', 'In-Active')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='vendor',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('on_hold', 'On Hold'), ('active', 'Active'), ('in-active', 'In-Active')], default='pending', max_length=20),
        ),
    ]
