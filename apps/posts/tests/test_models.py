from django.test import TestCase
from apps.posts.models import Post, Category


class PostModelTest(TestCase):
    """ This tests the post model """

    @classmethod
    def setUpTestData(cls): 

        #creating a post object
        Post.objects.create(
                            caption="Testing durrh",
                            description="wetin i go write here"
                            )
        
	
    def test_slug(self):
        """ tests slug field of the Post model""" 

        post = Post.objects.get(id=1)
        label = post._meta.get_field('slug').verbose_name
        size = post._meta.get_field('slug').max_length
        field_value = post.slug
        self.assertEquals(label, 'slug')
        self.assertEquals(size, 255)
			

	def test_caption(self):
		""" tests caption field of the Post Model"""

		post = Post.objects.get(id=1)
		label = post._meta.get_field('caption').verbose_name
		size = post._meta.get_field('caption').max_length
		self.assertEquals(label, 'caption')
		self.assertEquals(size, 500)


        

    
