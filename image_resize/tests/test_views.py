import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_list_view(client):
    url = reverse('image_resize:image_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_view(client):
    url = reverse('image_resize:image_create')
    response = client.get(url)
    assert response.status_code == 200
