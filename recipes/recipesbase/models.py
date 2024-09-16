from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 100)
    descriptionCategory = models.TextField(null = True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    nameRecipe = models.CharField(max_length = 100)
    description = models.TextField(null = True)
    products = models.TextField(null = True)
    image = models.ImageField(upload_to = 'images/', default = 'default.jpg')
    steps = models.TextField(null = True)
    recipeCategory = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'recipes')

    def __str__(self):
        return self.nameRecipe
