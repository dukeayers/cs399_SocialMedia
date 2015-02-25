# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def add_data(apps, schema_editor):

        User = apps.get_model("social", "User")

        FirstName = ["Duke"]
        LastName = ["Ayers"]
        Username = ["dukeayers"]
        Password = ["password"]
        EmailAddress = ["duke@nau.edu"]

        for i in range(0,1):
            data = User(first_name = FirstName[i], last_name = LastName[i], username = Username[i], password = Password[i], email_address = EmailAddress[i])
            data.save()

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
