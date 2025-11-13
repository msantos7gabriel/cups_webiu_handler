
from django.urls import path
from printer import views

urlpatterns = [
    path('test/',  views.test, name='test'),
    path('upload/',  views.upload_print, name='upload'),
]
