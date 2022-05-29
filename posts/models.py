from django.db import models
import datetime


# Create your models here.
class Posts(models.Model):
    author_name = models.CharField(max_length=100)

    blog_title = models.CharField(max_length=200)
    posted_time = str(datetime.datetime.now())
    content_blog = models.CharField(max_length=2000)
    blog_photo = models.ImageField(upload_to="uploads/")