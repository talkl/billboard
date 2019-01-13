from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages

def index(request):
    return render(request, 'billboard_app/index.html')

@login_required
def billboard(request):
    if request.method == 'POST':
        post_data = {
            'title': request.POST.get('title', ''),
            'content': request.POST.get('content', ''),
            'author': request.user.id
        }
        form = PostForm(post_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post added successfully')
            return redirect('billboard_app:billboard')
        else:
            messages.error(request, 'Post was not added. check valid input')
    context = {
        'posts': Post.objects.all().order_by('-date_posted'),
        'today': timezone.now()
    }
    return render(request, 'billboard_app/billboard.html', context)
