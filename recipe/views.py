from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def index(request):
    latest_recipe_list = Recipe.objects.order_by('-pub_date')[:5]
    context = {"recipe_list": latest_recipe_list}
    return render(request, "recipe/index.html", context)

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get_object_or_404(pk=recipe_id)
    return render(request, "recipe/recipe_detail.html", {"r": recipe})