from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    pub_date = models.DateTimeField(auto_now=True)

