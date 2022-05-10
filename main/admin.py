from django.contrib import admin
from .models import License, Track, Genre, Album, Comment, PlayList


# Litsenziya uchun Admin panel tuzish
@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('user',)
    list_filter = ('user',)


# Janir uchun Admin panel tuzush
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


# Albom uchun Admin panel tuzush
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name')
    list_display_links = ('user',)
    list_filter = ('user',)



# Qo'shiq uchun Admin panel tuzush
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'create_at')
    list_display_links = ('user',)
    list_filter = ('genre', 'create_at')
    search_fields = ('user', 'genre__name')



# Komentariya uchun Admin panel tuzush
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'track')
    list_display_links = ('user',)



@admin.register(PlayList)
class PlayListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    list_display_links = ('user',)
    search_fields = ('user', 'tracks_title')


