from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
<<<<<<< HEAD
    path('', views.post_list, name='post_list'),
]
 
=======
]
>>>>>>> a9b958dd388019eda80a02135633f975e042f3c0
