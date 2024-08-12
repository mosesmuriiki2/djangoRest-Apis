from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField(null=True, help_text="Add bio here")