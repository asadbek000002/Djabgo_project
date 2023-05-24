from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class List_view(ListView):
    model = Post
    template_name = 'home.html'


class Detail_view(DetailView):
    model = Post
    template_name = 'post_detail.html'


class Create_view(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'author', 'body']


class Update_view(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']


class Delete_view(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
