from django.urls import path

from product.apps import ProductConfig
from product.views import BotListView, BotDetailView

app_name = ProductConfig.name

urlpatterns = [
    path('', BotListView.as_view(), name='list'),
    path('<int:pk>/', BotDetailView.as_view(), name='get'),
]
