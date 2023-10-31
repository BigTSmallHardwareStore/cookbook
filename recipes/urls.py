from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('recipes/', views.all_recipes, name="all_recipes"),
]
