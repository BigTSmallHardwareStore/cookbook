from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_icon = models.ImageField(upload_to='images/', blank=True)

    def __str__(self) -> str:
        return self.category_name

   
class Ingredient(models.Model):
    ingredient = models.CharField(max_length=220, unique=True)

    def __str__(self) -> str:
        return self.ingredient


class Unit(models.Model):
    unit = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.unit


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="categories", blank=True, null=True)
    description = RichTextField(blank=True)
    recipe_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientToRecipe', related_name='recipes')
    url_name = AutoSlugField(populate_from='recipe_name', editable=False, always_update=True)

    def __str__(self) -> str:
        return self.recipe_name
    

class IngredientToRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ingredient_amounts", on_delete=models.SET_NULL, null=True)
    ingredient = models.ForeignKey(Ingredient, related_name="ingredient_amounts", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)
