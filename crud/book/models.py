from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField( max_length=200)
    content = models.TextField()
    price = models.CharField(help_text="원", max_length=100)
    model_choice = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    grade = models.CharField(max_length=1, choices=model_choice)
    
    img = models.ImageField(null=True)
 

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()