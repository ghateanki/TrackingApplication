from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Task
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Task
    template_name = 'home.html'
    ordering = ['-post_date']
   # ordering = ['-id']


def home(request):
    tasks = Task.objects.all()
    return render(request, "home.html", {"tasks": tasks})


class ArticleDetailView(DetailView):
    model = Task
    template_name = 'article_details.html'

class AddProjectView(CreateView):
    model = Task
    form_class = PostForm
    template_name = 'add_post.html'


def add_project(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()

    return render(request, 'add_post.html', {"form":form})


class UpdatePostView(UpdateView):
    model = Task
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','task','body']

class DeletePostView(DeleteView):
    model = Task
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    #fields = ['title','task','body']

