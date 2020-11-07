from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Translation(models.Model):
    title = models.CharField(max_length=255)
    Input = models.TextField()
    CHOICES = ('Text to Binary', 'Text to Binary'), ('Binary to Text', 'Binary to Text')
    choice = models.CharField(max_length=155, choices=CHOICES, default='-----------')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('translation_detail', args = [str(self.id)])
