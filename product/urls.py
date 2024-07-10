from django.urls import path

from product.apps import ProductConfig
from product.views import bot_list

app_name = ProductConfig.name

urlpatterns = [
    path('', bot_list, name='list'),
]
