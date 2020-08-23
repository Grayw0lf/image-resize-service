import os
from urllib.request import urlretrieve
from sorl.thumbnail import get_thumbnail

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.core.files import File
from django.core.files.base import ContentFile
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ImageCreateForm, ImageResizeForm, ResizeForm
from .models import Image


class ImageListView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'image_resize/image_list.html'


class ImageDetailView(UpdateView):
    model = Image
    form_class = ResizeForm
    context_object_name = 'image'
    template_name = 'image_resize/image_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ImageResizeForm'] = ResizeForm
        context['image_id'] = Image.objects.get(pk=self.kwargs['pk']).pk
        return context

    def form_valid(self, form):
        image_width = form.cleaned_data["image_width"]
        image_height = form.cleaned_data["image_height"]
        image = Image.objects.get(pk=self.kwargs['pk']).image_name
        resized = get_thumbnail(image, f"{image_width}x{image_height}")
        image.save(image.name, ContentFile(resized.read()), True)
        return super().form_valid(form)


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
                    filename = os.path.basename(image_url)
                    image_model.image_name.save(filename, File(open(result[0], 'rb')))
                    image_model.save()
                except:
                    err_mess = "В данной ссылке нет картинки"
                    return render(request, 'image_resize/image_create.html',
                                  context={'ImageCreateForm': form, 'err_mess': err_mess})
            elif image_file:
                image_model.image_name = form.cleaned_data["image_file"]
                image_model.save()
            return HttpResponseRedirect(reverse('image_resize:image_detail', args=(image_model.pk,)))

        context = {'ImageCreateForm': form}
        return render(request, 'image_resize/image_create.html', context)
