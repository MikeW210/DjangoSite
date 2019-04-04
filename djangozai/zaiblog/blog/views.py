from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/Home.html', context)
# Create your views here.
def about( request ):
    return  render(request, 'blog/About.html', {'title':'About'} )