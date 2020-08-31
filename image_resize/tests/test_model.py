import pytest
from image_resize.models import Image


@pytest.mark.django_db
def test_create_image():
    image = Image.objects.create(
        image_original='images/original/test.jpg',
        image_name='images/test.jpg',
        image_width=100,
        image_height=100
    )
    count = Image.objects.count()
    assert str(image) == 'test.jpg'
    assert image.filename() == 'test.jpg'
    assert image.image_original == 'images/original/test.jpg'
    assert image.image_name == 'images/test.jpg'
    assert image.image_width == 100
    assert image.image_height == 100
    assert count == 1
