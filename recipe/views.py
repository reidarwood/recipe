from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm, InstructionForm, IngredientForm
from django.forms.formsets import formset_factory



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})

# Create your views here.
def index(request):
    latest_recipe_list = Recipe.objects.order_by('-pub_date')[:5]
    context = {"recipe_list": latest_recipe_list}
    return render(request, "recipe/index.html", context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.views += 1
    recipe.save()
    return render(request, "recipe/recipe_detail.html", {"r": recipe})

def add_recipe(request):
    InstructionFormSet = formset_factory(InstructionForm, extra=3,
                                    min_num=1, validate_min=True)
    IngredientFormSet = formset_factory(IngredientForm, extra=3,
                                    min_num=1, validate_min=True)
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        ingredients = IngredientFormSet(request.POST)
        instructions = InstructionFormSet(request.POST)
        if all([form.is_valid(), ingredients.is_valid(), instructions.is_valid()]):
            rec = form.save()

            # go through all the ingredients and save
            for ingredient in ingredients:
                if ingredient.cleaned_data:
                    i = ingredient.save(commit=False)
                    i.recipe = rec
                    i.save()
            # instructions
            for num, instruction in enumerate(instructions):
                if instruction.cleaned_data:
                    i = instruction.save(commit=False)
                    i.recipe = rec
                    i.priority = num
                    i.save()
            return render(request, "recipe/recipe_detail.html", {"r": rec})
    else:
        form = RecipeForm()
        instructionFormset = InstructionFormSet()
        ingredientFormset = IngredientFormSet()

    return render(request, 'recipe/add_recipe.html', 
        {'form': form, 'instructionformset': instructionFormset,
         'ingredientformset': ingredientFormset})