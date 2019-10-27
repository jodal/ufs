# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-10-27 20:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounting", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="admins",
            field=models.ManyToManyField(
                blank=True, to=settings.AUTH_USER_MODEL, verbose_name="admins"
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="email",
            field=models.EmailField(
                blank=True,
                help_text="Contact address for group.",
                max_length=254,
            ),
        ),
    ]
