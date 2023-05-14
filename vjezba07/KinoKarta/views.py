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



def create_tickets(request, projekcija_id, user_id):
    projekcija = Projekcija.objects.get(id=projekcija_id)

    if request.method == 'POST':
        if projekcija.capacity > Karta.objects.filter(seat=projekcija.capacity).count():
            # Get the next available seat number
            next_seat = Karta.objects.filter(seat=projekcija.capacity).count() + 1 - projekcija.capacity

            # Get the user based on the provided user_id
            user = User.objects.get(id=user_id)

            # Create a new ticket for the specified user and projection
            ticket = Karta(seat=next_seat, movie=projekcija, user=user)
            projekcija.capacity =projekcija.capacity -1
            projekcija.save() 
            ticket.save()

            return redirect('ticket_success')
        else:
            return render(request, 'ticket_sold_out.html')

    return render(request, 'create_tickets.html', {'projekcija': projekcija})


