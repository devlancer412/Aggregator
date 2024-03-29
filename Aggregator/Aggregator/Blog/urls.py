from django.urls import path
from . import views

urlpatterns = [
  path('', views.create_blog, name='create-blog'),
  path('search/', views.search_blog, name='search-blog'),
  path('update/<int:pk>', views.update_blog, name='update-blog'),
  path('delete/<int:pk>', views.remove_blog, name='remove-blog'),
]