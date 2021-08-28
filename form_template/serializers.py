from .models import Category, Template
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields=("name",)
        model = Category


class TemplateSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Template
        fields = ('name', 'created', 'category', 'description', 'link',)
        depth = 1