from datetime import datetime, timezone

from django.db import models
from django.db.models.signals import post_save


class Category(models.Model):
    """this models a tag"""
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


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
        return str(self.country)


class Post(models.Model):
    """this class models a post object"""
    slug = models.SlugField(max_length=150, unique=True)
    caption = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
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

    def __str__(self):
        return self.caption


# a function that clears items that had been in the db 
# for 2mins or more(for the purpose of testing)
def clear_items(sender, instance, created, **kwargs):
    if created:
        items = Post.objects.all()

        if items:
            for item in items:
                date_created = item.date_created
                current_date = datetime.now(timezone.utc)
                time_delta = current_date - date_created
                minutes = time_delta.total_seconds() / 60

                if minutes >= 2:
                    item.delete()


#this signal calls the clear_items function
#each time a new item is created
post_save.connect(clear_items, sender=Post)
