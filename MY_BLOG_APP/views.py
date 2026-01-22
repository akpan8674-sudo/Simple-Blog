from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    allPosts = Post.objects.all().order_by('-created_at')
    context = {'posts': allPosts}
    return render(request, 'blog/home.html', context)

def register (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('MY_BLOG_APP:register-page')

        User_check = User.objects.filter(username=username).first()
        if User_check:
            messages.error(request, "Username already exists.")
            return redirect('MY_BLOG_APP:register-page')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('MY_BLOG_APP:login-page')

    return render(request, 'blog/register.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('MY_BLOG_APP:home')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('MY_BLOG_APP:login-page')

    return render(request, 'blog/login.html')

def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        author = request.user

        Post.objects.create(title=title, content=content, image=image, author=author)
        messages.success(request, "Post created successfully.")
        return redirect('MY_BLOG_APP:home')

    return render(request, 'blog/create_post.html')

def view_post(request, post_id):
    post_instance = get_object_or_404(Post, id=post_id)
    comments = post_instance.comments.all().order_by('-commented_at')
    context = {'post': post_instance, 'comments': comments}
    return render(request, 'blog/view_post.html', context)


def edit_post(request, post_id):
    post_instance = get_object_or_404(Post, id=post_id)

    if post_instance.author != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('MY_BLOG_APP:home')

    if request.method == "POST":
        post_instance.title = request.POST.get('title')
        post_instance.content = request.POST.get('content')
        post_instance.save()
        messages.success(request, "Post updated successfully.")
        return redirect('MY_BLOG_APP:home')

    context = {'post': post_instance}
    return render(request, 'blog/edit_post.html', context)

def delete_post(request, post_id):
    post_instance = get_object_or_404(Post, id=post_id)

    if post_instance.author != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('MY_BLOG_APP:home')

    post_instance.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect('MY_BLOG_APP:home')


def add_comment(request, post_id):
    post_instance = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        content = request.POST.get('content')
        
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect('MY_BLOG_APP:login-page')
        
        if content:
            Comment.objects.create(post=post_instance, author=request.user, content=content)
            messages.success(request, "Comment added successfully.")

        else:
            messages.error(request, "Comment content cannot be empty.")


    return redirect('MY_BLOG_APP:view-post', post_id=post_id)

def delete_comment(request, comment_id):
    comment_instance = Comment.objects.get(id=comment_id, author=request.user)
    comment_instance.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect('MY_BLOG_APP:home')

def logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('MY_BLOG_APP:home')