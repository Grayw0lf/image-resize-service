from django import forms


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


class ImageResizeForm(forms.Form):
    width = forms.IntegerField(label='Ширина', required=False,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.IntegerField(label='Высота', required=False,
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean(self):
        error_string = ''

        width = self.data.get('width', False)
        height = self.data.get('height', False)

        if any([width, height]):
            try:
                res = int(width)
            except:
                if width != '':
                    error_string += '"Ширина" должна быть числовым значением. '

            try:
                res = int(height)
            except:
                if height != '':
                    error_string += '"Высота" должна быть числовым значением. '

            if error_string != '':
                raise forms.ValidationError(error_string)
