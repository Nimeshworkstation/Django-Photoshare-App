from django.urls import path
from . import views

urlpatterns =[
	path('',views.gallery, name = 'gallery'),
	path('add/',views.add_photo, name = 'addphoto'),
	path('photo/<str:pk>/',views.view_photo, name = 'viewphoto'),
]