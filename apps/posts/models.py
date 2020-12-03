from django.db import models
from apps.core.utils import generate_unique_slug


class Category(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    caption = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="post_pictures", null=True, blank=True)
    date_created =  models.DateTimeField(auto_now_add=True)
    #will figure out how to do the expiration thing here

    def __str__(self):
        return self.caption