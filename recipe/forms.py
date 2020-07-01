from django import forms
from .models import Recipe, Instruction, Ingredient #come back to this
from datetime import datetime

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'author', )

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ('description', )

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'amount', )