from .views import fees_view
from django.urls import path

urlpatterns = [
    path('', fees_view, name='fees'),
]
