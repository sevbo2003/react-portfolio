from django.db import models
from django.utils.text import slugify


class Music(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    image = models.ImageField(upload_to='music-images')
    link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-added',)
        verbose_name = 'music'
        verbose_name_plural = 'Musics'


class Design(models.Model):
    name = models.CharField(max_length=210)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='design-images')
    link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def time(self):
        time = self.added
        return time.strftime("%B %-d, %Y")

    class Meta:
        ordering = ('-added',)
