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


@pytest.mark.image_resize_form
class TestImageResizeForm:
    def test_resize_form_image_width_field_label(self):
        form = ResizeForm()
        assert form.fields['image_width'].label == 'Ширина'

    def test_resize_form_image_height_field_label(self):
        form = ResizeForm()
        assert form.fields['image_height'].label == 'Высота'
