from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    length = models.FloatField()
    image = models.ImageField(upload_to='music-images')
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


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    download_link = models.URLField()
    size = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def time(self):
        time = self.added
        return time.strftime("%B %-d, %Y")

    @property
    def image_size(self):
        return str(self.size) + ' mb'

    class Meta:
        ordering = ('-added',)
        verbose_name = 'image'
        verbose_name_plural = 'Gallery'
