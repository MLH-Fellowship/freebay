from rest_framework import generics, viewsets, mixins, filters

from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from apps.posts.models import Post, Category, Location, Country
from apps.posts.api.serializers import PostSerializer

from apps.core.utils import generate_unique_slug


class ItemsViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet
                    ):
    """ This automatically generates list, create and retrieve
        endpoints for items. 

        for post requests, this endpoint expects the data
        sent to be in the format below:

        {
            "caption": "eg. sample testing 3 oh",
            "email": "some email here",
            "description": "eg. hihihihihi hahahahaha",
            "country": "eg. Nigeria",
            "city": "eg. Lagos"
            "category": "eg. food",
            "image": "image ur here"
        }
    """

    queryset = Post.objects.all().order_by("-date_created")
    lookup_field = 'slug'
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'description']

    def perform_create(self, serializer):
        cat = self.request.data["category"] 
        cnry = self.request.data["country"]
        cty = self.request.data["city"]
        caption = self.request.data["caption"]

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
        category = get_object_or_404(Category, title=cat)
        slug = generate_unique_slug(caption)
        serializer.save(
                        slug=slug,
                        category=category, 
                        location=location_obj
                        )
