from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = image = models.ImageField(default='default.jpg', upload_to='media/')

    def __str__(self):
        return self.name