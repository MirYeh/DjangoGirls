from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect


# list of post from db
def post_list(request):
    #QuerySet:
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# specific post details
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  #filter(pk=pks)
    return render(request, 'blog/post_detail.html', {'post': post})

# add new Post using a form
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #commit=false: don't save model yet
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# edit a new Post using a form
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
