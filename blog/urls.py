from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404
from .models import Post

urlpatterns = [
   path ('blog/', views.post_list, name= 'post_list'), 

]   

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
