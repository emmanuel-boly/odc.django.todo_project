# Generated by Django 4.1.5 on 2023-04-19 09:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="completed",
        ),
    ]
