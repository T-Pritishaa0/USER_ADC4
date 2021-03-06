from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    Title = models.CharField(max_length=250)
    Caption = models.CharField(max_length=500)
    File = models.FileField(upload_to="profile/photos/",default='ana.jpg')
    like = models.IntegerField(null=True, blank=True, default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")

    def __str__(self):
        return self.Caption


class Comment(models.Model):
    # image = models.ForeignKey(Post, on_delete=models.CASCADE)
    # user = models.ManyToManyField(User)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE, default=0)
    content = models.TextField(max_length= 660, default="Hello")
    


 
