from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES['recipe_image']
        print(data)
       
        Recipe.objects.create(
                recipe_name = recipe_name,
        recipe_description = recipe_description,
        recipe_image = recipe_image)  
        return redirect('/recipes/')
    queryset = Recipe.objects.all()
    context = {'recipes':queryset}
    return render(request,'recipes.html',context)
   
    
def delete_recipe(request,id):
    print(id)
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return HttpResponse("Recipe deleted successfully")
    return redirect('/recipes/')