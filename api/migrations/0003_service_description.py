# Generated by Django 5.0.2 on 2024-03-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_remove_client_user_remove_facture_service_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="service", name="description", field=models.TextField(null=True),
        ),
    ]
