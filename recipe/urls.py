from django.urls import path
from django.conf.urls import url
from mysite.core import views as core_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.add_recipe, name="create"),
    path('<int:recipe_id>', views.recipe_detail, name='detail'),
    url(r'^signup/$', core_views.signup, name='signup'),
]