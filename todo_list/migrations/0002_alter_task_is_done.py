# Generated by Django 4.1.7 on 2023-02-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo_list", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="is_done",
            field=models.BooleanField(default=False),
        ),
    ]
