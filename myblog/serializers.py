from rest_framework import serializers
from .models import Category, Post
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify
# import markdown


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'color',)


class SimplePostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        exclude = ('main_text',)


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    main_text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_main_text(self, instance):
        return mark_safe(markdownify(instance.main_text))
        # return markdown.markdown(instance.main_text, extensions=['markdown.extensions.toc'])
