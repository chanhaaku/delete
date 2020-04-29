from django.shortcuts import render , redirect
from .models import Post , Photo
from django.forms import modelformset_factory
from .forms import *
from django.views.generic import ListView , DetailView ,DeleteView , UpdateView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
	post = Post.objects.all()
	context={
		'post':post,
	} 
	return render(request , 'app/home.html',context)

def service(request):
	return render(request , 'app/service.html')

def about(request):
	return render(request ,'app/about.html')

def contact(request):
	return render(request , 'app/contact.html')

def ui(request):
	return render(request , 'app/mainui.html')

#creating post model form 
@login_required
def postview(request):
	ImageFormset = modelformset_factory(Photo , fields=('image',),extra=20)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		formset = ImageFormset(request.POST or None , request.FILES or None)
		if form.is_valid() and formset.is_valid():
			g=form.save(commit=False)
			g.save()

			for f in formset:
				try: 
					img=Photo(post = g,image = f.cleaned_data['image'])
					img.save()
				except Exception as e :
					break
		return redirect('home')

	else:
		form = PostForm
		formset = ImageFormset(queryset=Photo.objects.none())

	context = {
		'form':form,
		'formset':formset,
	}

	return render(request , 'app/post_create.html',context)






class TitleListView(ListView):
	model = Post 
	context_object_name = 'posts'
	template_name = 'app/title.html'



def titledetail(request , pk):
	post = Post.objects.get(id=pk)
	image = post.photo_set.all()
	context = {
				'post':post,
				'image':image,
				}

	return render(request ,'app/title_detail.html',context)


class PostDeleteView(LoginRequiredMixin,DeleteView):
	model = Post
	success_url = '/'

class PhotoDetailView(LoginRequiredMixin,DetailView):
	model = Photo
	template_name = 'app/test_detail.html'

#this is bugs has been fixed and working perfectly fine
class PhotoDeleteView(LoginRequiredMixin,DeleteView):
	model = Photo
	success_url = '/'


class TestListView(LoginRequiredMixin,ListView):
	model = Photo
	template_name = 'app/test.html'
	context_object_name = 'images'





# this is only for testing 



def testnav(request):
	return render(request , 'app/base2.html')



class CollectionListView(ListView):
	model = Post 
	context_object_name = 'posts'
	template_name = 'app/collection.html'


def titlesdetail(request , pk):
	post = Post.objects.get(id=pk)
	image = post.photo_set.all()
	context = {
				'post':post,
				'image':image,
				}

	return render(request ,'app/gallery.html',context)