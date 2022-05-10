from rest_framework import serializers
from .models import License, Album, Comment, Track, Genre, PlayList
from drf_settings.services import delete_old_file


class LicenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ('id', 'text',)


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'description', 'image', 'private')

        def update(self, instance, validated_data):
            delete_old_file(instance.image.path)
            return super().update(instance, validated_data)


# Aftir kiritadigan qo'shiqlar

class CreateAuthoTrackSerializer(serializers.ModelSerializer):
    plays_count = serializers.IntegerField(read_only=True)
    download = serializers.IntegerField(read_only=True)
    class Meta:

        model = Track
        fields = ('id', 'title', 'license', 'genre', 'album',
                  'link_of_author', 'file', 'create_at', 'plays_count', 'download')

        def update(self, instance, validated_data):
            delete_old_file(instance.file.path)
            return super().update(instance, validated_data)


class AuthorTrackSerializer(CreateAuthoTrackSerializer):

    license = LicenseSerializers()
    genre = GenreSerializers(many=True)
    album = AlbumSerializer()



