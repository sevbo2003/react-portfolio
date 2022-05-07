from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'blog category'
        verbose_name_plural = 'Blog category'


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post-images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'post'
        verbose_name_plural = 'Posts'


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=500)
    url = models.URLField()
    image = models.ImageField(upload_to='project-images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    @property
    def time(self):
        time = self.created
        return time.strftime("%B %-d, %Y")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'projects'
        verbose_name_plural = 'Projects'


class ChallengeName(models.Model):
    challenge = models.CharField(max_length=100)

    def __str__(self):
        return self.challenge


class Day30(models.Model):
    title = models.CharField(max_length=256)
    challenge = models.ForeignKey(ChallengeName, on_delete=models.CASCADE)
    day = models.IntegerField()
    description = models.CharField(max_length=500)
    body = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Day30, self).save(*args, **kwargs)

    @property
    def time(self):
        time = self.created
        return time.strftime("%B %-d, %Y")

    @property
    def url(self):
        return self.slug + '-' + f'day{self.day}'

    class Meta:
        ordering = ('-created',)
        verbose_name = '30 day'
        verbose_name_plural = '30 Day challenge'


class Thanks(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-added']
        verbose_name = 'thanks'
        verbose_name_plural = 'Thanks'

