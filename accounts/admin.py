from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm
from .models import User



# Register your models here.
class CustomUserAdmin(UserAdmin):
    form = SignUpForm
    model = User
    list_display = ('username',)

admin.site.register(User, CustomUserAdmin)
