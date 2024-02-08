from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, default='')
    published = models.BooleanField(default=True, blank=True)


    def __str__(self):
        return self.title


class Event(models.Model):
    picture = models.ImageField(null=True, blank=True, default=None)
    name = models.CharField(max_length=100)
    published = models.BooleanField(default=True, blank=True)


    def __str__(self):
        return self.name

class Gallery_Picture(models.Model):
    picture = models.ImageField(null=True, blank=True, default=None)
    published = models.BooleanField(default=True, blank=True)


    def __str__(self):
        return self.picture.url