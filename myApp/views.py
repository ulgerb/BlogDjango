from multiprocessing import context
from turtle import pos
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from myApp.models import *
from myApp.forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    posts = Post.objects.all()

    # Search start
    query = request.GET.get('q') 
    if query:
        posts = posts.filter(
            Q(name__icontains=query) | Q(name2__icontains=query) | Q(textpost__icontains=query)
        ).distinct()
    # Search end
    
    # paginator start
    paginator = Paginator(posts, 4) # bir sayfada kaç tane görüneceğini belirler
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 
    # paginator end
    context = {
        "posts": posts,
        "postsall": Post.objects.all(),
        "currentpost": CurrentPost.objects.all(),
        'category': Category.objects.all(),
        }
    
    return render(request, 'index.html', context)


# def indexRecent(request):
#     recent = Post.objects.all()
    
#     # bir sayfada kaç tane görüneceğini belirler
#     paginator = Paginator(recent, 8)
#     page = request.GET.get('page')
#     try:
#         recent = paginator.page(page)
#     except PageNotAnInteger:
#         recent = paginator.page(1)
#     except EmptyPage:
#         recent = paginator.page(paginator.num_pages)
#     context = {
#         "recent": recent
#     }
    
#     return render(request, 'index.html',context ) 
    
def about(request):
    
    # print(request.path) # alan adındaki url adresini çeker
    # print(request.get_full_path())
    
    return render(request, 'about.html')


def blog(request):
    posts = Post.objects.all()

    # bir sayfada kaç tane görüneceğini belirler
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    context= {
        'posts': posts,
        "postsall": Post.objects.all(),
        "currentpost": CurrentPost.objects.all(),
        'category': Category.objects.all(),
        }
    return render(request, 'blog.html',context )


def postDetails(request, pk):
    post = get_object_or_404(Post, pk=pk) # slug detail sayfası için seçili olan id alır
    # details = Post.objects.get(pk=pk) # slug detail sayfası için seçili olan id alır
    comments = post.comments.filter(approved_comment=True)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    
    context = {
        "postdetails": post,
        # "details": details,
        'comments': comments,
        'form' : form,
        "postsall": Post.objects.all(),
        "currentpost": CurrentPost.objects.all(),
        'category': Category.objects.all(),
        }
    return render(request, 'post-details.html', context)

# def add_comment_to_post(request, pk):
#     post = Post.get_object_or_404(Post, pk=pk)
#     form = CommentForm()
#     if request.POST == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post=post
#             comment.save()
#             return redirect('detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'forms.html', { 'form':form })

@login_required # bu işlemi yetkili yapabilir
def comment_approver(request,pk):
    comment = get_object_or_404(Comments, pk =pk)
    comment.approve()
    return redirect('detail', pk = comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    comment.delete()
    return redirect('detail', pk = comment.post.pk)
    
def contact(request):
    return render(request, 'contact.html')

def categoryShow(request, pk):
    posts = Post.objects.all()
    postpk = get_object_or_404(Category, pk=pk)
    
    print(postpk.title)
    context = {
        'postpk' : postpk,
        'posts' : posts,
        'category': Category.objects.all(),
    }
    return render(request, 'category.html', context)


