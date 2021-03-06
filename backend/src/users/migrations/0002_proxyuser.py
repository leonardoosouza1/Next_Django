# Generated by Django 3.2.10 on 2022-02-22 12:42

from django.db import migrations
from django.db import models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProxyUser",
            fields=[],
            options={
                "verbose_name": "user",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("users.user",),
            managers=[
                ("objects", users.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=30, verbose_name="First name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=50, verbose_name="Last name"),
        ),
    ]
