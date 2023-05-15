from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Projekcija, Karta
from django.contrib.auth.models import User
from .forms import ProjekcijaForm
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
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
    movies = Projekcija.objects.filter(id__in=tickets.values('movie_id'))

    context = {
        'user': user,
        'tickets': tickets,
        'movies': movies
    }
    return render(request, 'tickets.html', context)



def decrease_capacity(request, pk, user_id):
    # Retrieve the Projekcija object based on the primary key
    projekcija = get_object_or_404(Projekcija, pk=pk)
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        if projekcija.capacity > 0:
            # Decrease the capacity by one
            projekcija.capacity -= 1
            projekcija.save()
            
            karta = Karta(seat=projekcija.capacity, movie=projekcija, user=user)
            karta.save()

            # Redirect or render appropriate template
            return redirect('/movies/')
        else:
            # Capacity is already full, handle accordingly
            return render(request,'ticket_sold_out.html')
    context = {
        'projekcija': projekcija,
        'user_id': user_id
    }

    # Render the form template
    return render(request, 'decrease.html', context)


def delete_ticket(request, user_id, movie_id):
    try:
        user = User.objects.get(pk=user_id)
        movie = Projekcija.objects.get(pk=movie_id)

        # Filter the Karta table based on user and movie
        karta = Karta.objects.filter(user=user, movie=movie)

        if karta.exists():
            # Delete the Karta entry
            Projekcija.objects.filter(pk=movie_id).update(capacity=F('capacity') + 1)
            karta.delete()
            return redirect('/movies/')  # Redirect to appropriate page after deletion
    except ObjectDoesNotExist:
        context = {
            'user_id': user_id,
            'movie_id': movie_id,
        }
        return render(request, 'no_ticket.html', context)  # Render a template for not found case

    # If no exception occurred and the ticket was not found, redirect to appropriate page
    return redirect('/movies/')
