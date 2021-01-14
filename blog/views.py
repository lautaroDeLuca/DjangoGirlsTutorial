from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(datePublished__lte=timezone.now()).order_by('-datePublished')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_details(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'posts' : posts})