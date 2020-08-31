import pytest
from image_resize.forms import ImageCreateForm, ResizeForm


@pytest.mark.image_create_form
class TestImageCreateForm:
    def test_image_create_url_field_label(self):
        form = ImageCreateForm()
        assert form.fields['image_url'].label == 'Ссылка'

    def test_image_create_file_field_label(self):
        form = ImageCreateForm()
        assert form.fields['image_file'].label == 'Файл'

    def test_image_create_file_valid(self):
        image_file = 'images/original/test.jpg'
        data = {'image_file': image_file}
        form = ImageCreateForm(data=data)
        assert form.is_valid()

    def test_image_create_url_valid(self):
        image_url = 'http://test.com/test.jpg'
        data = {'image_url': image_url}
        form = ImageCreateForm(data=data)
        assert form.is_valid()

    def test_image_create_empty_fields(self):
        data = {'image_file': '',
                'image_url': ''}
        form = ImageCreateForm(data=data)
        assert not form.is_valid()


@pytest.mark.image_resize_form
class TestImageResizeForm:
    def test_resize_form_image_width_field_label(self):
        form = ResizeForm()
        assert form.fields['image_width'].label == 'Ширина'

    def test_resize_form_image_height_field_label(self):
        form = ResizeForm()
        assert form.fields['image_height'].label == 'Высота'
