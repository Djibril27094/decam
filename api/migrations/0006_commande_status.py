# Generated by Django 5.0.2 on 2024-03-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_client_addresse"),
    ]

    operations = [
        migrations.AddField(
            model_name="commande",
            name="status",
            field=models.CharField(
                choices=[
                    ("choix1", "Choix 1"),
                    ("choix2", "Choix 2"),
                    ("choix3", "Choix 3"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]