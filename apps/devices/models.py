from django.db import models


class MySetup(models.Model):
    image = models.ImageField(upload_to='my-current-setup')
    active = models.BooleanField(default=True)
