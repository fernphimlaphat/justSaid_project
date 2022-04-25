from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.

#def home(request):
#    return render(request, 'home.html',{})

# Home page
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'