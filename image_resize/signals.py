from django.db.models.signals import post_save
from django.dispatch import receiver
from pathlib import Path
import os
from .models import Image


@receiver(post_save, sender=Image)
def resize_image_rename(sender, instance, created, **kwargs):
    if created:
        new_path = Path(instance.image_name.name).parent / Path(instance.image_original.name).name
        os.rename(Path(instance.image_name.name), new_path)
        instance.image_name.name = new_path
        instance.save()