from django.core.exceptions import ValidationError
import os
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'current_page_namber': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'items_page': len(self.page),
            'results': data
        })


# User uchun Rasm fayli
def get_path_uploads_image(instance, file):

    return f"image/user_{instance}/{file}"


# Cover albom uchun rasm fayl
def get_path_uploads_cover_album(instance, file):

    return f"image/user_{instance.user.id}/{file}"

# Play list uchun fayl
def get_path_uploads_play_list(instance, file):

    return f"image/playlist_{instance.user.id}/{file}"


# Qo'shiq uchun fayl
def get_path_uploads_track(instance, file):

    return f"track/user_{instance.user.id}/{file}"

def validate_size_image(file_obj):

    megabayt_limit = 2
    if file_obj.size > megabayt_limit * 1024 *1024:
        raise ValidationError(f"Eng katta razmerlik fayl{megabayt_limit}MB")


def delete_old_file(paht_file):
    if os.path.exists(paht_file):
        os.remove(paht_file)