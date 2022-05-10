from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('genre/', views.GenreListAPIVew.as_view(), name='genre'),

    path('license/', views.LicenseViewset.as_view({'get': 'list', 'post': 'create'})),
    path('license/<int:pk>/', views.LicenseViewset.as_view({'put': 'update', 'delete': 'destroy'})),

    path('album/', views.AlbumViewset.as_view({'get': 'list', 'post': 'create'})),
    path('album/<int:pk>/', views.AlbumViewset.as_view({'put': 'update', 'delete': 'destroy'})),

    path('author-album/<int:pk>/', views.PublicAlbum.as_view(), name='author-album'),

    path('track/', views.TrackViewsets.as_view({'get': 'list', 'post': 'create'})),
    path('track/<int:pk>/', views.TrackViewsets.as_view({'put': 'update', 'delete': 'destroy'})),

    path('track-list/', views.TrackListAPIView.as_view(), name='track-list'),
    path('author-track-list/<int:pk>/', views.AuthorTrackListAPIView.as_view(), name='author-track-list'),

    path('stream-track/<int:pk>/', views.StreamingFileView.as_view(), name='stream-track'),
    path('download-track/<int:pk>/', views.DownloadTraclViews.as_view(), name='download-track')
]