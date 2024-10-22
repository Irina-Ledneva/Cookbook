from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15, unique=True, verbose_name='Имя')
    password = models.CharField(max_length=15, verbose_name='Пароль')
    user_date_add = models.DateField(auto_now_add=True,
                                     verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Categories(models.Model):
    category_name = models.CharField(max_length=30, blank=True,
                                     verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Recipes(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING,
                                 verbose_name='Категория')
    recipe_name = models.CharField(max_length=100, verbose_name='Название')
    recipe_description = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    stages_preparation = models.TextField(verbose_name='Этапы приготовления')
    time_preparation = models.IntegerField(
        verbose_name='Время приготовления, мин.')
    food_image = models.ImageField(upload_to='food_images', blank=True,
                                   verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                               verbose_name='Автор')

    def __str__(self):
        return self.recipe_name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
