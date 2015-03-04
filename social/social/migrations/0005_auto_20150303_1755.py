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
        
        user = User.objects.create_user("nancy", "nancym@nau.edu", "password")
        user.first_name = "Nancy"
        user.last_name = "McCollough"
        user.save()

        user = User.objects.create_user("admin", "admin@vidyabook.com", "password")
        user.first_name = "Admin"
        user.save()
        
        # a sample post to test the database
        Content = apps.get_model("social", "Content")
        post = Content(url="http://shshatteredmemories.com/", description="lol!", userid=5, datetime="2003-08-04 12:30:45", image="http://i.imgur.com/6XI9cDR.jpg")
        post.save()

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
