from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Projekcija, Karta
from django.contrib.auth.models import User
from .forms import ProjekcijaForm
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

def create_movies(request):
    if request.method == 'POST':
        form = ProjekcijaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create/')  # Redirect to the '/create/' URL
    else:
        form = ProjekcijaForm()

    return render(request, 'create_movies.html', {'form': form})

