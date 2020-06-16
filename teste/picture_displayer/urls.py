from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Pictures_Home'),
    path('add/', views.add_image, name='Add_picture'),
    path('<int:pk>', views.view_image, name='view_image'),
    path('delete/<int:pk>', views.delete_image, name='delete_image'),
]
