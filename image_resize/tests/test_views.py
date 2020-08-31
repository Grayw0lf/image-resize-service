import pytest
from django.urls import reverse
from image_resize.models import Image


@pytest.mark.django_db
def test_list_view(client):
    image1 = Image.objects.create(
        image_original='images/original/test1.jpg',
        image_name='images/test1.jpg',
        image_width=100,
        image_height=100
    )
    image2 = Image.objects.create(
        image_original='images/original/test2.jpg',
        image_name='images/test2.jpg',
        image_width=100,
        image_height=100
    )
    url = reverse('image_resize:image_list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['images']) == 2


@pytest.mark.django_db
def test_create_view(client):
    url = reverse('image_resize:image_create')
    response = client.get(url)
    assert response.status_code == 200
    assert 'ImageCreateForm' in response.context


@pytest.mark.django_db
def test_image_update_detail_view(client):
    image = Image.objects.create(
        image_original='images/original/test.jpg',
        image_name='images/test.jpg',
        image_width=100,
        image_height=100
    )
    url = reverse('image_resize:image_update', kwargs={'pk': image.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert 'ImageResizeForm' in response.context
