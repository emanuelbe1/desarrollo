# Generated by Django 4.2.5 on 2023-09-10 01:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Models",
            new_name="Post",
        ),
    ]