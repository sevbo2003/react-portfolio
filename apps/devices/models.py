from django.db import models


class MySetup(models.Model):
    image = models.ImageField(upload_to='my-current-setup')
    active = models.BooleanField(default=True)


class DailyUses(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    url = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.type
