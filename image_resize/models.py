from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from sorl.thumbnail import ImageField as SorlImageField, get_thumbnail


class Image(models.Model):
    image_name = SorlImageField(_('Изображение'), upload_to='images',
                                width_field='image_width',
                                height_field='image_height',
                                blank=True, null=True
                                )
    image_width = models.PositiveIntegerField(null=True, blank=True)
    image_height = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')

    def filename(self):
        return Path(self.image_name.name).name

    def __str__(self):
        return self.filename()

    def get_absolute_url(self):
        return reverse('image_resize:image_update', args=[self.pk])


