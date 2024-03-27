from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("""<h1 style="color:red">This is a recipe project</h1>
#                         <hr>
#                         <p>This is coming from django server</p>""")


def home(request):
    peoples = [
        {'name':'Abhijit','age':30},
        {'name':'Rani','age':35},
        {'name':'vicky','age':25}
    ]

    for people in peoples:
        print(people)

    return render(request,'index.html',context = {'peoples':peoples})