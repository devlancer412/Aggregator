from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html', {"insert_me": "I'm from view.py"})

def viewArticle(request, articleId):
  text = "Displaying article number: %s"%articleId
  return HttpResponse(text)
  
def showarticle(request, msg):
    return render(request, 'result.html', {'msg' : msg})