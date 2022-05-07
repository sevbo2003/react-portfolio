from django.db import models


class MySetup(models.Model):
    image = models.ImageField(upload_to='my-current-setup')
    active = models.BooleanField(default=True)


class DailyUses(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    url = models.URLField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'daily used item'
        verbose_name_plural = 'Daily uses'

    def __str__(self):
        return self.type


class Accessories(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    url = models.URLField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Aksessuar'
        verbose_name_plural = 'Aksessuars'

    def __str__(self):
        return self.type


class Development(models.Model):
    type = models.CharField(max_length=80)
    name = models.CharField(max_length=100)
    url = models.URLField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Development tool'
        verbose_name_plural = 'Development tools'

    def __str__(self):
        return self.type


class Keyboard(models.Model):
    image = models.ImageField(upload_to='keyboards')
    url = models.URLField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'keyboard'
        verbose_name_plural = 'Keyboards'
        ordering = ('-added',)

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=201)
    link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-added',)
