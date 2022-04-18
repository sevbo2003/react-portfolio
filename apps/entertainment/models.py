from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    length = models.FloatField()
    link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    @property
    def uzunligi(self):
        return f"{self.length} mins"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-added',)
        verbose_name = 'music'
        verbose_name_plural = 'Musics'
