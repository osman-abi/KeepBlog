from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # fields = ('first_name','last_name','username','email')
    search_fields = ['email','username','first_name']
    list_display = ['first_name','last_name','username','email']
    list_filter = ['email','username']