# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.models import User

class Migration(migrations.Migration):

    def add_data(apps, schema_editor):
        user = User.objects.create_user("duke", "duke@nau.edu", "password")
        user.first_name = "Duke"
        user.last_name = "Ayers"
        user.save()

        user = User.objects.create_user("admin", "admin@vidyabook.com", "password")
        user.first_name = "Admin"
        user.save()

    operations = [
        migrations.RunPython(add_data)
    ]
