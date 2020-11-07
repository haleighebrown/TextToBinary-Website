from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User

class Translation(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('translation_detail', args = [str(self.id)])
