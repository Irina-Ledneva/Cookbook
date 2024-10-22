from django.urls import path
from .views import *

urlpatterns = [path('', index, name='home'),
               path('categories/', categories, name='categories'),
               path('all_recipes/', all_recipes, name='all_recipes'),
               path('recipes/', recipes, name='recipes'),
               path('add_recipe/', add_recipe, name='add_recipe'),
               path('entrance/', entrance, name='entrance'),
               path('registration/', registration, name='registration'),
               path('add_category/', add_category, name='add_category'),
               path('recipes/<int:recipe_id>/', one_recipe, name='one_recipe'),
               path('categories/<int:category_id>/', category_recipes, name='category_recipes'),
               path('all_recipes/delete/<int:id>', delete_recipe)]