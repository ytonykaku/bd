# Generated by Django 4.2.7 on 2023-12-05 04:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0002_estadosbrasil_alter_statstime_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="statstime",
            options={"managed": False},
        ),
    ]
