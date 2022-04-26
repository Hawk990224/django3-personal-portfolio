from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    try:
        n = int(request.GET.get('n'))
        blogs = Blog.objects.order_by('-date')[:n]
    except Exception as e:
        blogs = Blog.objects.all()
        n = blogs.count
    return render(request, 'blog/all_blogs.html', {'blogs':blogs, 'show_n':n})

# Create your views here.
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    print(blog)
    return render(request, 'blog/detail.html', {'blog':blog})
