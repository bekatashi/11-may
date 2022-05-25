from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.BasketApiView.as_view())
]