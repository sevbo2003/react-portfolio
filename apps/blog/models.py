from django.db import models
from ckeditor.fields import RichTextField
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    body = RichTextField()
    image = models.ImageField(upload_to='post-images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @property
    def time(self):
        time = self.created
        return time.strftime("%B %-d, %Y")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'post'
        verbose_name_plural = 'Posts'


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=500)
    body = RichTextField()
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
