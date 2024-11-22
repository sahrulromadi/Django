from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Menampilkan field yang diinginkan
    list_display = ('username', 'email', 'age', 'profile_picture', 'is_staff', 'is_active')
    # Filter pencarian
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
