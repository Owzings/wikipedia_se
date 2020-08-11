from django.shortcuts import render
from titre_wiki.models import Titre
import wikipedia
from elasticsearch import Elasticsearch 


es=Elasticsearch([{'host':'localhost','port':9200}])
es

# Create your views here.
def titles(request): 
    
    titles = wikipedia.search("Tennis", results = 100, suggestion = True)
    for a in titles:
        title = Titre(titre=a)
        title.save()
    
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Titre.objects.all() 
    
          
    return render(request, "title.html", context) 