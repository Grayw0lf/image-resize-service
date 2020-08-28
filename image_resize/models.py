from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from sorl.thumbnail import ImageField as SorlImageField
from .storage import OverwriteStorage


class Image(models.Model):
    image_original = models.ImageField(_('Оригинальное изображение'),
                                       upload_to='images/original',
                                       blank=True, null=True
                                       )
    image_name = SorlImageField(_('Изображение'), storage=OverwriteStorage(),
                                upload_to='images',
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
        return self.image_name.name

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        # self.image_name.name = str(Path(self.image_name.name).parent/Path(self.image_original.name).name)

    def get_absolute_url(self):
        return reverse('image_resize:image_update', args=[self.pk])
