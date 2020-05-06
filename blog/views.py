from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

# ページの見た目をここで作る。

def post_list(request):
    contents = {
        'posts': Post.objects.all().order_by('-created_date')
    }
    return render(request, 'blog/post_list.html', contents)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pablished_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})