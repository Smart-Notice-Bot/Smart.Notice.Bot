from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .models import Comment
from .forms import BlogUpdate
from accounts.models import User, AdminType

import logging
logger=logging.getLogger(__name__)

def home(request):
    blogs = Blog.objects.order_by('-id')
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'home.html', {'blogs':blogs,'posts':posts} )

def management(request):
    user = User.objects.filter(admin_type=AdminType.USER)
    return render(request, 'management.html', {'users': user})

def edit(request):
    return render(request, 'edit.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog = blog_id)
    if request.method =='POST':
        comment = Comment()
        comment.blog = blog_detail
        comment.body = request.POST['body']
        comment.date = timezone.now()
        comment.save()
    return render(request, 'detail.html', {'blog': blog_detail, 'comments':comments})

def create(request):
    return render(request, 'create.html')

def postcreate(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    try:
	    blog.image = request.FILES['image']
    except:
	    blog.image = None
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/faq/detail/' + str(blog.id))

def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method =='POST':
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('/faq/detail/' + str(blog.id))
    else:
        form = BlogUpdate(instance = blog)
 
        return render(request,'update.html', {'form':form})


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def new(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'new.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )

def search(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "") 

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html', {'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'search.html')