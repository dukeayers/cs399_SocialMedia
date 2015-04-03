# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_content_tags'),
    ]

    operations = [
	
		migrations.CreateModel(
			name='Userpic',
			fields=[
			('username', models.CharField(max_length=30)),
			('url', models.URLField()),
			],
			options={
			},
			bases=(models.Model,),
		),
    ]
