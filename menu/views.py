from django.shortcuts import render, get_object_or_404
from .models import Category, Food

def home(request):
    categories = Category.objects.all()
    return render(request, 'menu/base.html', {'categories': categories})

def food_by_category(request, category_name):
    categories = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    foods = Food.objects.filter(category=category)
    return render(request, 'menu/base.html', {
        'categories': categories,
        'selected_category': category,
        'foods': foods,
    })