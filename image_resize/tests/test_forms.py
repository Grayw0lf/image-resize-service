from image_resize.forms import ImageCreateForm, ResizeForm


def test_image_create_url_field_label():
    form = ImageCreateForm()
    assert form.fields['image_url'].label == 'Ссылка'


def test_image_create_file_field_label():
    form = ImageCreateForm()
    assert form.fields['image_file'].label == 'Файл'


def test_resize_form_image_width_field_label():
    form = ResizeForm()
    assert form.fields['image_width'].label == 'Ширина'


def test_resize_form_image_height_field_label():
    form = ResizeForm()
    assert form.fields['image_height'].label == 'Высота'
