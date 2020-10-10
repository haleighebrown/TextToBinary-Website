from django.db import models

class Translation(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    ##body = models.TextFields()

    def __str__(self):
        return self.title
