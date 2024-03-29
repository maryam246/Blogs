from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post, Category


# Create your views here.
def home(request):
    # load all the post from db(10)
    post = Post.objects.all()[:11]
    # print(post)
    cats= Category.objects.all()
    data= {
        'post':post,
        'cats':cats
    }
    return render(request,'home.html',data)

def post(request,url):
    post_url = Post.objects.get(url=url)
    # print(post_url)
    cats = Category.objects.all()
    return render(request, 'post.html', {'post_url':post_url, 'cats':cats})

def category(request,url):
    cat= Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, 'category.html', {'cat':cat,  'posts':posts})
