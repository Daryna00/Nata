from django.urls import path
from .views import index, page


urlpatterns = [
    path('', index, name='homepage'),
    path('page', page, name='page'),
    ]