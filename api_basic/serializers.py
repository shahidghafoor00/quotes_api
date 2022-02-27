from rest_framework import serializers
from .models import Quote


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'author', 'quote']

