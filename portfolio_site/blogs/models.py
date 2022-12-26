from django.db import models

# Create your models here.
class BlogPosting(models.Model):
    blog_heading = models.CharField(max_length=100)
    blog_text = models.CharField(max_length=1000)
    date_published = models.DateTimeField('date published')
    images = models.CharField(max_length=500) # you will be storing the path to the images in your project
                                              # in this model field as strings. you will use this path in the
                                              # src attribute for any html tags that need it
    def __str__(self):
        return self.blog_heading