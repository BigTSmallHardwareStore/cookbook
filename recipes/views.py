from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "recipes/index.html")


def all_recipes(request):
    return render(request, "recipes/all_recipes.html", {
        "recipes": Recipe.objects.all(),
        #"categories": Category.objects.all()
    })




def show_recipe(request, url_name):
    try:
        recipe = Recipe.objects.filter(url_name=url_name)[0]   
    except:
        return HttpResponseRedirect(reverse("all_recipes"))

    ingredients = IngredientToRecipe.objects.filter(recipe=recipe)

    return render(request, "recipes/recipe.html", {
        "recipe": recipe,
        "ingredients": ingredients
    })
