from django.db import models


class BookCategory(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'book category'
        verbose_name_plural = 'Book Categories'


STATUS_BOOK = (
    ('read', 'read'),
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
        ordering = ('added',)
        verbose_name = 'book'
        verbose_name_plural = 'Books'
