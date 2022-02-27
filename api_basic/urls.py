from django.urls import path, include
from .views import article_list

urlpatterns = [
    path('quotes/', article_list),
]
