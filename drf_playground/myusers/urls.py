from . import views
from django.urls import path

urlpatterns = [
    path('', views.handle_users),
]
