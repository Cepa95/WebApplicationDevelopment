"""
URL configuration for kino project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from KinoKarta import views
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('KinoKarta/hello', views.say_hello),
    path('__debug__/', include('debug_toolbar.urls')),
    path('movie/', views.movies),
    path('create/', views.create_movies),
    path('movies/', views.sve_projekcije),
    path('tickets/<int:user_id>/', views.user_tickets, name='user_tickets'),
    path('decrease/<int:pk>/<int:user_id>/', views.decrease_capacity, name='decrease_capacity'),
    path('delete_ticket/<int:user_id>/<int:movie_id>/', views.delete_ticket, name='delete_ticket'),
    # path('create_tickets/<int:projekcija_id>/<int:id>', views.create_tickets, name='create_tickets'),
]
