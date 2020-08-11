from django.shortcuts import render
from article_wiki.models import Article
from titre_wiki import Titre
import wikipedia

# Create your views here.

def articles(request): 
    
    titles = Titre.objects.all() 
    for a in titles:
        title = Titre(titre=a)
        title.save()
    
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Article.objects.all() 
    
          
    return render(request, "articles.html", context) 