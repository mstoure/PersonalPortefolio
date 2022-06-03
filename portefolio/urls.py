from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.current_datetime, name='current_datetime'),
]