from django.shortcuts import render
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES['recipe_image']
        print(data)
    print(recipe_name)
    print(recipe_description)
    print(recipe_image)
    Recipe.objects.create(
        recipe_name = recipe_name,
        recipe_description = recipe_description,
        recipe_image = recipe_image
    )
    return render(request,'recipes.html')