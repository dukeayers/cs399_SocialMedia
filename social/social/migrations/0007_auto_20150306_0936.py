# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.models import User
from datetime import datetime
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

        user = User.objects.create_user("ktaed", "ktaed@nau.edu", "password")
        user.first_name = "Tsosie"
        user.last_name = "Schneider"
        user.save()

        user = User.objects.create_user("admin", "admin@vidyabook.com", "password")
        user.first_name = "Admin"
        user.save()
        
        # a sample post to test the database
        Content = apps.get_model("social", "Content")
        post = Content(url="http://shshatteredmemories.com/", description="Lordy!", username="nancy", datetime=datetime.now(), image="http://i.imgur.com/6XI9cDR.jpg")
        post.save()

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
