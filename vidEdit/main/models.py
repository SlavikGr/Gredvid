from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=130)
    picture = models.ImageField(upload_to='images/')
    body_title = models.CharField(max_length=50, default="Body_title")
    body = models.TextField(default='Body')
    link = models.TextField(default='Ссылка на видео')

    def __str__(self):
        return self.title
