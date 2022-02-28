from django.urls import path

from exam.main_app.views import index_view, add_album_view, edit_album_view, delete_album_view, album_details_view, \
    profile_details_view, profile_create_view, delete_profile_view

urlpatterns = [
    path('', index_view, name='index page'),
    path('add/', add_album_view, name='add album page'),
    path('edit/<int:pk>', edit_album_view, name='edit album page'),
    path('delete/<int:pk>', delete_album_view, name='delete album page'),
    path('details/<int:pk>', album_details_view, name='album details page'),

    path('profile/details/', profile_details_view, name='profile details page'),
    path('profile/', profile_create_view, name='create profile page'),
    path('profile/delete/', delete_profile_view, name='delete profile page'),
]