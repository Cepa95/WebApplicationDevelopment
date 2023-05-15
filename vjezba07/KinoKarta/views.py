from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Projekcija, Karta
from django.contrib.auth.models import User
from .forms import ProjekcijaForm
from django.db.models import Max
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


def sve_projekcije(request):
    projekcije = Projekcija.objects.all()
    return render(request, 'projekcije.html', {'projekcije': projekcije})


def user_tickets(request, user_id):
    user = User.objects.get(id=user_id)
    tickets = Karta.objects.filter(user=user)
    context = {
        'user': user,
        'tickets': tickets
    }
    return render(request, 'tickets.html', context)


from django.shortcuts import get_object_or_404, render, redirect
from .models import Projekcija, Karta



def decrease_capacity(request, pk):
    # Retrieve the Projekcija object based on the primary key
    projekcija = get_object_or_404(Projekcija, pk=pk)

    if request.method == 'POST':
        if projekcija.capacity > 0:
            # Decrease the capacity by one
            projekcija.capacity -= 1
            projekcija.save()

            # Redirect or render appropriate template
            return redirect('/movies/')
        else:
            # Capacity is already full, handle accordingly
            return render(request,'ticket_sold_out.html')

    # Render the form template
    return render(request, 'decrease.html', {'projekcija': projekcija})
