from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<recipe_id>', views.recipe_detail, name='detail')
]