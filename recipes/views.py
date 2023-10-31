from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "recipes/index.html")

def show_recipe(request):
    return render(request, "recipes/recipe.html")

def all_recipes(request):
    return render(request, "recipes/all_recipes.html")
