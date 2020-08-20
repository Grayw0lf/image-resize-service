from django.urls import path
from .views import ImageListView, ImageCreateView, ImageDetailView


app_name = 'image_resize'

urlpatterns = [
    path('', ImageListView.as_view(), name='image_list'),
    path('image/create/', ImageCreateView.as_view(), name='image_create'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
]