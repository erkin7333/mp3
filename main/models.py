from django.core.validators import FileExtensionValidator
from django.db import models
from account.models import User




# Litsenziya uchun model
from drf_settings.services import validate_size_image, get_path_uploads_cover_album, get_path_uploads_track, \
    get_path_uploads_play_list


class License(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lincenses', blank=True, null=True)
    text = models.TextField(max_length=1500)

    def __str__(self):
        return self.user.username


# Qo'shiq Janiri uchun model

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# Qo'shiq uchun Albom modeli

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='albums')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)
    private = models.BooleanField(default=False)
    image = models.ImageField(upload_to=get_path_uploads_cover_album, validators=[FileExtensionValidator(),
                                                                                  validate_size_image])
    def __str__(self):
        return f"{self.user.username} {self.name}"



# Trek qo'shiq modeli

class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='tracks')
    title = models.CharField(max_length=100)
    license = models.ForeignKey(License, on_delete=models.PROTECT, related_name='license_tracks')
    genre = models.ManyToManyField(Genre, related_name='track_genres')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)
    link_of_author = models.CharField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to=get_path_uploads_track,
                            validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
    create_at = models.DateTimeField(auto_now_add=True)
    plays_count = models.PositiveIntegerField(default=0)
    download = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    user_of_likes = models.ManyToManyField(User, related_name='likes_of_tracks')

    def __str__(self):
        return f"{self.user} - {self.title}"



# Qo'shiq uchun komentariya modeli

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='track_comment')
    text = models.TextField(max_length=2000)
    create_at = models.DateTimeField(auto_now_add=True)


# Ijro ro'yxati uchun model

class PlayList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='play_lists')
    title = models.CharField(max_length=50)
    tracks = models.ManyToManyField(Track, related_name='track_play_list')
    image = models.ImageField(upload_to=get_path_uploads_play_list)

