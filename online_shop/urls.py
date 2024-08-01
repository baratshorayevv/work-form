

from django.urls import path, include
from . import views
urlpatterns = [
    path('index/', views.product_list, name='product_list'),
    path('', include('online_shop.urls')),
]
