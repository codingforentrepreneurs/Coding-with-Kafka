# Generated by Django 5.0.3 on 2024-03-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="is_shipped",
            field=models.BooleanField(default=False),
        ),
    ]
