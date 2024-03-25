from django.shortcuts import render, HttpResponseRedirect
from .models import Category, Photo
from .forms import AddPhoto, AddCategory
# Create your views here.
def gallery(request):
	categories = Category.objects.all()
	photos = Photo.objects.all()
	return render(request,'phots/gallery.html',{'categories':categories,'photos':photos})

def add_photo(request):
	categories = Category.objects.all()
	if request.method == 'POST':
		data = request.POST
		image = request.FILES.get('image')

		if data['category'] != 'none':
			category = Category.objects.get(id=data['category'])

		elif data['category_new'] != '':
			category = Category.objects.get_or_create(name=data['category_new'])
		else:
			category = None

		photo = Photo.objects.create(
			category=category,
			description=data['description'],
			image=image,

			)

	return render(request,'phots/add.html',{'cat':categories})

def view_photo(request,pk):
	photo = Photo.objects.get(id=pk)
	return render(request,'phots/photo.html',{'photo':photo})
	
