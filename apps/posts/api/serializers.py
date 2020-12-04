from rest_framework import serializers
from apps.posts.models import Post, Location


class LocationSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Location
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    slug = serializers.SlugField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    location = LocationSerializer(read_only=True)
    email = serializers.EmailField(max_length=254)

    class Meta:
        model = Post
        exclude = ["date_created"]
