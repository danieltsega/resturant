from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This points to our homepage
    path('category/<str:category_name>/', views.food_by_category, name='food_by_category'),
]
