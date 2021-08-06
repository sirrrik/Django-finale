from os import pipe
from django.shortcuts import render
from .models import posts
from subprocess import run,PIPE
import sys
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    Posts = posts.objects.all()[:20]
   

    context = {
        'title': 'Latest Posts',
        'posts': Posts

    }

    return render(request, 'posts/index.html',context)

def extenal(request):
     v = run(sys.executable,'//home//victor//Desktop//projects//Django@finale//speech.py', shell=True,stdout=PIPE)

     return render(request,'posts/index.html', {'data':v})



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

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_Name']
        last_name = request.POST['last_Name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print('user created')
        

    else:
        return render(request, 'posts/register.html')    
    return render( request,'posts/register.html')