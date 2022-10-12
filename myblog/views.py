from django.shortcuts import render
from .models import BlogPost
from .forms import NewBlog, Login
from django.http import HttpResponseRedirect

# Create your views here.

def posts(request):
    return render(request, 'posts.html', {
        'posts': BlogPost.objects.all(),
        'page_name': 'Posts'
    })

def home(request):
    return render(request, 'home.html', {
        'page_name': 'Home'
    })

def new_post(request):
    submitted = False
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_post?submitted=True')
    else:
        form = NewBlog 
        if 'submitted' in request.GET:
            submitted = True
            
        

    form = NewBlog
    return render(request, 'newPost.html', {
        'page_name': 'Add Post',
        'form': form,
        'submitted': submitted,
    })

def login(request):
    form = Login
    return render(request, 'login.html', {'form': form,
                                            'page_name' : 'Login'})