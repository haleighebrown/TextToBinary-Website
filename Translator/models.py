from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Translation(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField(default = None)
    date = models.DateTimeField(default = True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('translation_detial', args = [str(self.id)])
