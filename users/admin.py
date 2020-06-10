from django.contrib import admin
from .models import Profile, Follow, Ban



@admin.register(Follow)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'follow_user', 'date']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']

@admin.register(Ban)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['who_blocking', 'blocked_users']

