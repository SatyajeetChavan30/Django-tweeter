from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tweet (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(("Enter your tweetuu"), max_length=240)
    photo = models.ImageField(("Choose a photo"), upload_to='photos/', blank= True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f"{self.user.username} - {self.text[:30]}"
    
class contact_me (models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    text = models.TextField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    