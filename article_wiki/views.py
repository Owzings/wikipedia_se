from django.shortcuts import render
from article_wiki.models import Article
from titre_wiki.models import Titre
import wikipedia
import time

# Create your views here.

def articles(request): 
    
    titles = Titre.objects.all() 
    
    for a in titles:
        b = wikipedia.page(a.titre)
        articles = Article(titre=a, content=b.content)
        time.sleep(60)
        articles.save()

    
    context ={} 
  
    # # add the dictionary during initialization 
    context["dataset"] = Article.objects.all() 
    
          
    return render(request, "articles.html", context) 