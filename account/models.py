from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from drf_settings.services import get_path_uploads_image, validate_size_image

# User model Foydalanuvchii malumotlari


class User(AbstractUser):
    name = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to=get_path_uploads_image, default='./images.png',
                              validators=[FileExtensionValidator(), validate_size_image])
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email


# Obunachilar
class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', blank=True, null=True)
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber', blank=True, null=True)

    def __str__(self):
        return f"{self.subscriber} obunachi {self.user}"


# Ijtimoiy havolalar
class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_link', blank=True, null=True)
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.user