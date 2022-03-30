from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog

# Create your views here.
def create_blog(request):
  if request.method == 'POST':
    form = BlogForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('search/')
      except:
        pass
  else:
    form = BlogForm()
  return render(request, 'create.html', {'form': form})
  
def search_blog(request):
  blogs = Blog.objects.all()
  return render(request, 'search.html', {'blogs': blogs})

def update_blog(request, pk):
  blogs = Blog.objects.get(id=pk)
  form = BlogForm(instance=blogs)

  if request.method == 'POST':
    form = BlogForm(request.POST, instance=blogs)
    if form.is_valid():
      form.save()
      return redirect('/blog/search')
  
  context = {
    'blogs': blogs,
    'form': form,
  }

  return render(request, 'update.html', context)

def remove_blog(request, pk):
  blogs = Blog.objects.get(id=pk)
  form = BlogForm(blogs)

  if request.method == 'POST':
    blogs.delete()
    return redirect('/blog/search')

  context = {
    'blogs': blogs
  }

  return render(request, 'remove.html', context)