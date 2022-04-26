from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

# Create your views here.

#def home(request):
#    return render(request, 'home.html',{})

# Home page
class HomeView(ListView):
    model = Post
    form_class = PostForm
    template_name = 'home.html'
    ordering =['-post_date']
    #ordering =['id'] #เรียงโพสตามID->เลขมากอยู่ล่าง

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #field = {'title','body'}

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #field = {'title','body'}
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
