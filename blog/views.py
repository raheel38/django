from django.shortcuts import render

from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/blog_list.html', {})

