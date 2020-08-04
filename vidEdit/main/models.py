from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=130)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
