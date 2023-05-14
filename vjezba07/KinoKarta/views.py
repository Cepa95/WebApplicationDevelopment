from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def say_hello(request):
#     return HttpResponse('Hello')

def say_hello(request):
    return render(request, 'hello.html', { 'name': 'Josip' })

movies_list = [{"name":"Batman", "year": 2022, "genre":"Adventure"}, 
    {"name":"Spiderman", "year": 2019, "genre":"Adventure"}, 
    {"name":"Spiderman2", "year": 2022, "genre":"Adventure"}, 
    {"name":"Dr.Strange", "year": 2022, "genre":"Adventure"},
    {"name":"Gentelman", "year": 2019, "genre":"Action"}, 
    {"name":"Snatch", "year": 2000, "genre":"Action"}] 

def movies(request):      
    return render(request,'movie_list.html', {"data":movies_list})