# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.URLField()),
                ('description', models.TextField(max_length=200)),
                ('userid', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('image', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]