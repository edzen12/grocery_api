from django.urls import path
from .views import CartView


urlpatterns = [
    path('api/cart/', CartView.as_view()),
]
