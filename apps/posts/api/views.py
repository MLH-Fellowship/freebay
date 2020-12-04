from rest_framework import generics, viewsets, mixins, filters

from rest_framework.generics import get_object_or_404

from apps.posts.models import Post, Category, Location, Country
from apps.posts.api.serializers import PostSerializer


class ItemsViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    ):
    """ This automatically generates list, create and retrieve
        endpoints for items.
    """

    queryset = Post.objects.all().order_by("-date_created")
    lookup_field = 'slug'
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        cat = self.request.data["category"] 
        cnry = self.request.data["country"]
        cty = self.request.data["city"]

        #this grabs and returns a country if it exists
        #if it doesn't a new instance is created, persisted 
        #in the db and then returned
        country_obj, _ = Country.objects.get_or_create(
                                                    name=cnry
                                                    )

        #this grabs and returns a location object if it exists
        #if it doesn't a new instance is created, persisted 
        #in the db and then returned
        location_obj, _ = Location.objects.get_or_create(
                                                    country=country_obj,
                                                    city=cty,
                                                    )
        category = get_object_or_404(Category, name=cat)

        serializer.save(
                        category=category, 
                        location=location_obj
                        )
