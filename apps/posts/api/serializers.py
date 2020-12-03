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

    class Meta:
        model = Post
        exclude = ["date_created"]

	def get_upvotes(self, object): return object.up_voters.count()

	def get_comments(self, object):
		return object.post_comments.count()

	def get_downvotes(self, object):
		votes = object.down_voters.count()

		if votes > 0:
			votes = votes * -1
		return votes

	def get_current_user_has_upvoted(self, object):
		request = self.context.get("request")
		request_user  = request.user
		return object.up_voters.filter(username = request_user.username).exists()

	def get_current_user_has_downvoted(self, object):
		request = self.context.get("request")
		request_user  = request.user
		return object.down_voters.filter(username=request_user.username).exists()