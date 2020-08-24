from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Image


class ImageCreateForm(forms.Form):
    image_url = forms.CharField(label='Ссылка',
                                widget=forms.URLInput(),
                                required=False)
    image_file = forms.ImageField(label='Файл', required=False)

    def clean(self):
        image_url = self.cleaned_data.get('image_url')
        image_file = self.cleaned_data.get('image_file')

        if image_url and image_file:
            raise forms.ValidationError('Заполненным может быть только одно поле')

        if image_url == '' and image_file is None:
            raise forms.ValidationError('Заполненным должно быть хотя бы одно поле')


class ResizeForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_width', 'image_height']
        labels = {
            'image_width': _('Ширина'),
            'image_height': _('Высота'),
        }
