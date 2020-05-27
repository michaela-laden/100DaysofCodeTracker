from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView
)
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'tracker/home.html')

def tracker(request):
    return render(request, 'tracker/index.html')

def stats(request):
    return render(request, 'tracker/stats.html')

def ideas(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'tracker/ideas.html', context)


# class PostListView(ListView):
#     model = Post
#     template_name = 'tracker/ideas.html'
#     context_object = 'posts'
#     ordering = ['-date_posted']

