from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello_page, name="hello_page"),
    path('base/', views.base_page, name="base"),
    path('admin/', admin.site.urls),
]