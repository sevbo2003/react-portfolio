from django.db import models


class BookCategory(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'book category'
        verbose_name_plural = 'Book Categories'


STATUS_BOOK = (
    ('read', 'Read'),
    ('reading', 'Reading'),
    ('will read', 'Read later')
)


class Book(models.Model):
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=300, help_text='The name of the book')
    description = models.CharField(max_length=400, help_text='A little about this book')
    status = models.CharField(choices=STATUS_BOOK, max_length=10)
    link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-added',)
        verbose_name = 'book'
        verbose_name_plural = 'Books'


TYPE_READING = (
    ('blog', 'blog'),
    ('article', 'article')
)


class Reading(models.Model):
    type = models.CharField(choices=TYPE_READING, max_length=7)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added',)
        verbose_name = 'Reading'
        verbose_name_plural = 'Reading'

    def __str__(self):
        return self.name


class Podcast(models.Model):
    name = models.CharField(max_length=200)
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


class Talk(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='talk-images')
    link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def image_link(self):
        return self.image.url

    @property
    def time(self):
        time = self.added
        return time.strftime("%B %-d, %Y")

    class Meta:
        ordering = ('-added',)


class Tutorial(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
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
