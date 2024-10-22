from random import choice

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'mainapp/index.html')


def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/add_recipe.html')
        return redirect('add_category')
    form = AddCategoryForm()
    return render(request, 'mainapp/add_category.html', {'form': form})


def recipes(request):
    recipes = Recipes.objects.all()
    if len(recipes) <= 5:
        data = {'recipes': recipes}
    else:
        new_recipes = []
        while len(new_recipes) < 5:
            el = choice(recipes)
            if not el in new_recipes:
                new_recipes.append(el)
        data = {'recipes': new_recipes}
    return render(request, 'mainapp/recipes.html', context=data)


def categories(request):
    categories = Categories.objects.all()
    return render(request, 'mainapp/categories.html',
                  {'categories': categories})


def category_recipes(request, category_id):
    category = Categories.objects.get(pk=category_id)
    recipes = Recipes.objects.filter(category=category)
    return render(request, 'mainapp/category_recipes.html',
                  {'recipes': recipes})


def one_recipe(request, recipe_id):
    try:
        recipe = Recipes.objects.get(pk=recipe_id)
    except:
        return redirect('recipes')
    data = {'recipe': recipe}
    return render(request, 'mainapp/one_recipe.html', context=data)


def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/successful_add_recipe.html')
        return redirect('recipes')
    form = AddRecipeForm()
    return render(request, 'mainapp/add_recipe.html', {'form': form})


def all_recipes(request):
    recipes = Recipes.objects.all()
    data = {'recipes': recipes}
    return render(request, 'mainapp/all_recipes.html', context=data)


def entrance(request):
    if request.method == 'POST':
        form = EntranceForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            dict_users = {}
            users = User.objects.all()
            for u in users:
                dict_users[u.username] = u.password
            if username in dict_users and dict_users[username] == password:
                return redirect('recipes')
            return redirect('entrance')
    else:
        form = EntranceForm()

    data = {'form': form}
    return render(request, 'mainapp/entrance.html', data)


def registration(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            users = User.objects.all()
            if users:
                users_list = [u.username for u in users]
                if username in users_list:
                    return render(request, 'mainapp/username_error.html')
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                user = User(username=username, password=password)
                user.save()
                return render(request, 'mainapp/successful_registration.html')
            return redirect('registration')
    else:
        form = LoginForm()

    data = {'form': form}
    return render(request, 'mainapp/registration.html', data)

def delete_recipe(request, id):
    recipe = Recipes.objects.get(id=id)
    recipe.delete()
    return redirect('recipes')

