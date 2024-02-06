# Generated by Django 4.2.9 on 2024-02-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0114_addons_flyout_sorting"),
    ]

    operations = [
        migrations.AddField(
            model_name="addonsconfig",
            name="flyout_sorting_stable_latest_at_beginning",
            field=models.BooleanField(
                default=True,
                help_text="Show <code>stable</code> and <code>latest</code> at the beginning",
            ),
        ),
    ]
