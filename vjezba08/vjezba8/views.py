from django.shortcuts import render, redirect
from .models import Korisnici
# Create your views here.

def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        role = request.POST['role']
        status = request.POST['status']

        if password != repeat_password:
            error_message = "Passwords do not match."
            return render(request, 'add_user.html', {'error_message': error_message})

        user = Korisnici.objects.create_user(username=username, password=password,
                                             first_name=first_name, last_name=last_name,
                                             email=email, role=role, status=status)
        # Additional processing or redirect to a success page
        return redirect('success_page')

    return render(request, 'add_user.html')
