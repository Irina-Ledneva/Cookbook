from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=25, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=25, label='Пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=25,
                                       label='Подтвердите пароль')


class EntranceForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=25, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=25, label='Пароль')


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['category_name']


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['category', 'recipe_name', 'recipe_description', 'ingredients', 'stages_preparation',
                  'time_preparation', 'food_image', 'author']
