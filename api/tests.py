from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import BlogPost, Person

class BlogPostAPITestCase(APITestCase):
    
    def setUp(self):
        # Set up data for the tests
        self.blog_post = BlogPost.objects.create(
            title="First Blog Post",
            content="This is the content of the first blog post."
        )
        self.url_list_create = reverse("blogpost-view-create")
        self.url_retrieve_update_destroy = reverse("update", args=[self.blog_post.pk])
        self.url_get_with_title = reverse("get")
    
    def test_create_blog_post(self):
        # Test creating a new blog post
        data = {
            "title": "New Blog Post",
            "content": "This is the content of the new blog post."
        }
        response = self.client.post(self.url_list_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)
    
    def test_list_blog_posts(self):
        # Test listing all blog posts
        response = self.client.get(self.url_list_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_retrieve_blog_post(self):
        # Test retrieving a specific blog post
        response = self.client.get(self.url_retrieve_update_destroy, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.blog_post.title)
    
    def test_update_blog_post(self):
        # Test updating a specific blog post
        data = {
            "title": "Updated Blog Post",
            "content": "This is the updated content."
        }
        response = self.client.put(self.url_retrieve_update_destroy, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.blog_post.refresh_from_db()
        self.assertEqual(self.blog_post.title, "Updated Blog Post")
    
    def test_delete_blog_post(self):
        # Test deleting all blog posts
        response = self.client.delete(self.url_list_create, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(), 0)
    
    def test_filter_blog_post_by_title(self):
        # Test filtering blog posts by title
        response = self.client.get(self.url_get_with_title, {'title': 'First'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.blog_post.title)

class PersonFormTestCase(APITestCase):
    
    def test_person_form(self):
        # Test if the person form renders correctly
        url = reverse("person")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'form')
