from django.contrib import admin
from .models import User, Follower, SocialLink



# User Admin Uchun
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'created_at',)
    list_display_links = ('email',)



# Ijtimoiy havolaalar uchun admin
@admin.register(SocialLink)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'link',)

