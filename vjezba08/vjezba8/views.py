from django.shortcuts import render, redirect
from .models import Korisnici
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.urls import reverse
# Create your views here.




def check_admin(user):
    return user.role == 'administrator'


@login_required
@user_passes_test(check_admin)
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
        return redirect('/success/')

    return render(request, 'add_user.html')



# def success(request):
#     return render(request, 'success.html')



# def success_student(request):
#     return render(request, 'success_student.html')


@login_required
def success_login(request):
    user = request.user
    if user.role == 'administrator':
        return render(request, 'success.html', {'user': user})
    elif user.role == 'student':
        return render(request, 'success_student.html', {'user': user})
    else:
        return render(request, 'success.html', {'user': user})   





@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse('login'))
    else:
        return render(request, 'logout.html')