from multiprocessing import context
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='hello'),
  path('article/<int:articleId>', views.viewArticle, name='article'),
  path('topics/<slug:msg>', views.showarticle, name = 'showarticle')
]