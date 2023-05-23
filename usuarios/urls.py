from django.urls import path, include

from usuarios import views


app_name = "usuarios"

urlpatterns = [
    path('', views.registro, name="registro"),
]