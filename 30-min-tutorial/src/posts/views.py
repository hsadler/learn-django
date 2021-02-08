from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "posts/index.html", context)