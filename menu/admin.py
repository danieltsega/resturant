from django.contrib import admin
from .models import Category, Food
from django.utils.html import format_html
from django.urls import path

# Register the Category model with enhanced admin features
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_count')
    search_fields = ('name',)
    
    # Method to show the count of food items in each category
    def food_count(self, obj):
        return obj.foods.count()
    food_count.short_description = 'Number of Foods'



@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'image_preview')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')
    autocomplete_fields = ['category']
    readonly_fields = ['image_preview']
    
    # Adding a thumbnail preview of the food image
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'


class FoodInline(admin.TabularInline):
    model = Food
    fields = ('title', 'price', 'image_preview', 'image')
    readonly_fields = ['image_preview']
    extra = 1


class CustomAdminSite(admin.AdminSite):
    site_header = "Restaurant Management"
    site_title = "Restaurant Menu Admin"
    index_title = "Welcome to the Restaurant Menu Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('admin/', self.admin_view(self.index))
        ]
        return custom_urls + urls

    def each_context(self, request):
        context = super().each_context(request)
        context['extra_css'] = ['admin/css/custom_admin.css']
        return context

# Initialize custom admin site
admin_site = CustomAdminSite(name='custom_admin')

admin.site.site_header = "Restaurant Management"
admin.site.site_title = "Restaurant Menu Admin"
admin.site.index_title = "Welcome to the Restaurant Menu Admin"


