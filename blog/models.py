from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from autoslug import AutoSlugField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural ='Categories'    

class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title',)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='post/thumbnail')
    description = RichTextField(null=True,blank=True)
    tags = models.TextField(null=True, blank=True)
    posted = models.DateField(default=datetime.now,null=True,blank=True)
    is_published = models.BooleanField(default=False)



    def __str__(self):
        return self.title

class Like(models.Model):

    particular_post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    name = models.CharField(max_length=100)
    likes = models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return str(self.likes)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"





class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE ,related_name="comments")
    name = models.CharField(max_length=100)
    comments = models.TextField(max_length=100,default='')
    email = models.EmailField(max_length=100,null=True,blank=True)
    created = models.DateTimeField(default=datetime.now)
    weburl = models.CharField(max_length=100,null=True,blank=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    