from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect

# Create your views here.
def value(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())







    form = PostForm()
    als = Post.objects.all()
    return render(request,'index.html',{'als':als})

def home(request):
    return render(request,'home.html')