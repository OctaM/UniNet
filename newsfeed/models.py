from django.db import models
from login.models import User


# this is the model for a 'stire' from newsfeed
class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=3000)
    link = models.CharField(max_length=1000, blank=True)
    photos = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.text