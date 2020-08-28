from django.apps import AppConfig


class ImageResizeConfig(AppConfig):
    name = 'image_resize'

    def ready(self):
        from . import signals
