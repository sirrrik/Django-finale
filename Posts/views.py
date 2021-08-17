from os import pipe
from django.shortcuts import redirect, render
from .models import posts
from subprocess import run,PIPE
import sys
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# show the the posts im the database 
def index(request):
    Posts = posts.objects.all()[:20]
   

    context = {
        'title': 'Latest Posts',
        'posts': Posts

    }

    return render(request, 'posts/index.html',context)

# call and run the speech.py file on button click
def extenal(request):
     v = run(sys.executable,'//home//victor//Desktop//projects//Django@finale//speech.py', shell=True,stdout=PIPE)

     return render(request,'index.html', {'data':v})


# get the stored posts in the database
def post(request, id):
    Post = posts.objects.get(id=id)

    context = {
        'post': Post
    } 

    return render(request, 'posts/post.html',context)

def about(request):
    
    return render( request,'posts/about.html')

def contact(request):
    
    return render( request,'posts/contact.html')

# register the users into the database with the defualt django usercreation templete
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'posts/register.html')  
            

    else: 
        form = UserCreationForm()        
    args = {'form':form}
    return render(request, 'posts/register.html', args)
        
