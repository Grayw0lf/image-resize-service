from pathlib import Path
from urllib.request import urlretrieve
from sorl.thumbnail import get_thumbnail

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.core.files import File
from django.core.files.base import ContentFile
from django.views.generic import ListView, CreateView, UpdateView

from .forms import ImageCreateForm, ResizeForm
from .models import Image


class ImageListView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'image_resize/image_list.html'


class ImageUpdateView(UpdateView):
    model = Image
    form_class = ResizeForm
    context_object_name = 'image'
    template_name = 'image_resize/image_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = self.get_object()
        width = image.image_width
        height = image.image_height
        context['ImageResizeForm'] = ResizeForm(initial={'image_width': width,
                                                         'image_height': height})
        return context

    def form_valid(self, form):
        image_width = form.cleaned_data["image_width"]
        image_height = form.cleaned_data["image_height"]
        image = self.get_object()
        if (image_width is None and image_height is None) \
                or (image_width == image.image_width and image_height == image.image_height):
            return HttpResponseRedirect(reverse('image_resize:image_update', args=(image.pk,)))
        if image_width is None:
            image_width = image.image_width
        if image_height is None:
            image_height = image.image_height
        resized = get_thumbnail(image.image_name, f"{image_width}x{image_height}", quality=100)
        image.image_name.save(Path(image.image_name.name).name, ContentFile(resized.read()), True)
        return HttpResponseRedirect(reverse('image_resize:image_update', args=(image.pk,)))


class ImageCreateView(CreateView):
    template_name = 'image_resize/image_create.html'

    def get_context_data(self, **kwargs):
        context = {'ImageCreateForm': ImageCreateForm}
        return context

    def post(self, request):
        form = ImageCreateForm(request.POST, request.FILES)

        if form.is_valid():
            image_url = form.cleaned_data["image_url"]
            image_file = form.cleaned_data["image_file"]
            image_model = Image()
            err_mess = False
            if image_url:
                try:
                    result = urlretrieve(image_url)
                    filename = Path(image_url).name
                    image_model.image_name.save(filename, File(open(result[0], 'rb')))
                    image_model.save()
                except:
                    err_mess = "В данной ссылке нет картинки"
                    return render(request, 'image_resize/image_create.html',
                                  context={'ImageCreateForm': form, 'err_mess': err_mess})
            elif image_file:
                image_model.image_name = form.cleaned_data["image_file"]
                image_model.save()
            return HttpResponseRedirect(reverse('image_resize:image_update', args=(image_model.pk,)))

        context = {'ImageCreateForm': form}
        return render(request, 'image_resize/image_create.html', context)
