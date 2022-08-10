from multiprocessing import context
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from myApp.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from myApp.forms import *
# Create your views here.

def index(request):
    posts = Post.objects.all()
    # Search 
    query = request.GET.get('q') 
    if query:
        posts = posts.filter(
            Q(name__icontains=query) | Q(name2__icontains=query) | Q(textpost__icontains=query)
        ).distinct()
    # Search end
    
    paginator = Paginator(posts, 3) # bir sayfada kaç tane görüneceğini belirler
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 
        
    context = {"posts": posts}

    return render(request, 'index.html', context)

    
    
def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def postDetails(request, idler):
    post = Post.objects.all()
    detail = Post.objects.get(pk=idler) #slug detail sayfası için seçili olan id alır
    form = CommentForm(request.POST or None)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url)
    
    context = {
        "postdetails": post,
        "postdetail" : detail,
        'form' : form,
        }
    return render(request, 'post-details.html', context)


def contact(request):
    return render(request, 'contact.html')

# def category_show(request):
#     context = {
#         'category' : 
#     }

