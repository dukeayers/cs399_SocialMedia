from social.models import Content
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ContentSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()
    datetime = serializers.DateTimeField(format='%m-%d-%Y')

    class Meta:
        model = Content
        fields = ('url', 'description', 'username', 'datetime', 'image', 'tags', 'pk')
