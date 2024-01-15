from django.urls import path
from .views import home_page, news,news2

urlpatterns = [
    path('', home_page),
    path('news/', news),
    path('news2/', news2)
]
