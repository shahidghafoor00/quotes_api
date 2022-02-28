from django.urls import path, include
from .views import quote_list

urlpatterns = [
    path('quotes/', quote_list),
]
