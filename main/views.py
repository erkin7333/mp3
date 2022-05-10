import os.path
from django.http import FileResponse, Http404
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import permissions, parsers
from .models import Genre, License, Album, Track
from drf_settings.services import delete_old_file, Pagination
from drf_settings.mixin_classes import MixedSerializer
from .serializers import (GenreSerializers, LicenseSerializers, AlbumSerializer,
                          CreateAuthoTrackSerializer, AuthorTrackSerializer)



# ModelViewSet yordamida CRUD amalari

class LicenseViewset(ModelViewSet):
    permission_classes = permissions.AllowAny
    serializer_class = LicenseSerializers

    def get_queryset(self):
        return License.objects.first(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ModelViewSet yordamida CRUD amalari Albom modeli ustida

class AlbumViewset(ModelViewSet):

    serializer_class = AlbumSerializer
    parser_classes = (parsers.MultiPartParser,)

    def get_queryset(self):
        return Album.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.image.path)
        instance.delete()


# Umumiy albomda yoqlarni userni o'ziga tegishli bo'lganlarinii chiqarish

class PublicAlbum(ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.filter(user__id=self.kwargs.get('pk'), private=False)


class TrackViewsets(MixedSerializer, ModelViewSet):

    parser_classes = (parsers.MultiPartParser, )
    serializer_class = CreateAuthoTrackSerializer
    serializer_classes_by_action = {
        'list': AuthorTrackSerializer
    }

    def get_queryset(self):
        return Track.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        delete_old_file(instance.image.path)
        instance.delete()


# Qo'shiqlarni List shaklida chiqarish

class TrackListAPIView(ListAPIView):
    queryset = Track.objects.all()
    serializer_class = AuthorTrackSerializer
    pagination_class = Pagination


# Aftir o'zi qo'shgan qo'shiqni bazadan olish ListAPIView usullida

class AuthorTrackListAPIView(ListAPIView):

    serializer_class = AuthorTrackSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return Track.objects.filter(user__id=self.kwargs.get('pk'))


# JAnrlarni ListAPIView Yordamida bazadan olish

class GenreListAPIVew(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers




class StreamingFileView(APIView):

    def set_play(self, track):
        track.plays_count += 1
        track.save()


    def get(self, request, pk):
        track = get_object_or_404(Track, id=pk)
        if os.path.exists(track.file.path):
            self.set_play(track)
            return FileResponse(open(track.file.path, 'rb'), filename=track.file.path)
        else:
            return Http404


class DownloadTraclViews(APIView):

    def set_download(self):
        self.track.download += 1
        self.track.save()

    def get(self, request, pk):
        self.track = get_object_or_404(Track, id=pk)
        if os.path.exists(self.track.file.path):
            self.set_download()
            return FileResponse(open(self.track.file.path, 'rb'), filename=self.track.file.path, as_attachment=True)
        else:
            return Http404