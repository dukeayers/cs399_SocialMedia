# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('social', '0007_auto_20150306_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
