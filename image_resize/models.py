import os
from django.urls import reverse
from django.db import models


class Image(models.Model):
    image_name = models.ImageField(upload_to='images')

    def filename(self):
        return os.path.basename(self.image_name.name)

    def __str__(self):
        return self.filename()

    def get_absolute_url(self):
        return reverse('image_resize:image_detail', args=[self.pk])
