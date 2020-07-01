from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.add_recipe, name="create"),
    path('<int:recipe_id>', views.recipe_detail, name='detail'),
    
]