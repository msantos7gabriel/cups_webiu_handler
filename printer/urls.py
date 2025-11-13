
from django.urls import path
from printer import views

urlpatterns = [
    path('test/',  views.test, name='test'),
]
