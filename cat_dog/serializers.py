from rest_framework import serializers
from cat_dog.models import MyImages


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyImages
        fields = ('id', 'myfile', 'title')
