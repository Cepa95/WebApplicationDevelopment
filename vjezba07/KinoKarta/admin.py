from django.contrib import admin
from .models import Projekcija, Karta
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

#na admin konzoli mi daj novu tablicu
admin.register(Projekcija)
admin.register(Karta)

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

#da dobiju id
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)