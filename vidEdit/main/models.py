from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
