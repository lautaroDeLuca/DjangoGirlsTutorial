from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(datePublished__lte=timezone.now()).order_by('datePublished')
    return render(request, 'blog/post_list.html', {'posts' : posts})