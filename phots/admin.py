from django.contrib import admin
from .models import Photo, Category

@admin.register(Photo)
class Photo(admin.ModelAdmin):
	list_display = ['id','category','image','description']

@admin.register(Category)
class Category(admin.ModelAdmin):
	list_display = ['name']
