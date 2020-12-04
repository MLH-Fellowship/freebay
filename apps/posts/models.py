from django.db import models
from apps.core.utils import generate_unique_slug


class Category(models.Model):
    """this models a tag"""
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Country(models.Model):
    """this models a country"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    """this models a location"""
    country = models.ForeignKey(
                                  Country, 
                                  on_delete=models.SET_NULL,
                                  related_name="cities", 
                                  null=True, 
                                  blank=True
                                  )
    city = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.country+", "+self.city


class Post(models.Model):
    """this class models a post object"""
    slug = models.SlugField(max_length=150, unique=True)
    caption = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
                                  Category, 
                                  on_delete=models.SET_NULL, 
                                  related_name="items",
                                  null=True, 
                                  blank=True
                                  )
    location = models.ForeignKey(
                                  Location, 
                                  on_delete=models.SET_NULL,
                                  related_name="posts", 
                                  null=True, 
                                  blank=True
                                  )
    image = models.ImageField(
                                upload_to="post_pictures", 
                                null=True, 
                                blank=True
                                )
    date_created =  models.DateTimeField(auto_now_add=True)
    #will figure out how to do the expiration thing here

    #customizing the default save method
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        slug = generate_unique_slug(self.caption)
        self.slug = slug

    def __str__(self):
        return self.caption
