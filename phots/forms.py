from django import forms
from .models import Photo, Category

class AddPhoto(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ['category','image','description']

class AddCategory(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']