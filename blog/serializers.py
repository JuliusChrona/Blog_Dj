from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField()
    views = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'views', 'category')