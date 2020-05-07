from django.shortcuts import render
from cookbook.models import Recipe, Author


# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def author_detail(request, id):
    person = Author.objects.get(id)
    recipe = Recipe.objects.filter(author=person)
    return render(request, 'author.html', {'person': person, 'recipe': recipe})

def recipe_detail(request, id):
    recipe = Recipe.objects.filter(id)
    return render(request, 'recipe.html', {'recpie': recipe})