from django.urls import path
from .views import *


urlpatterns = [
    path('api/products/', ProductView.as_view()),
    path('api/category/', CategoryView.as_view()),
    path('api/demo/', DemoView.as_view()),
]
