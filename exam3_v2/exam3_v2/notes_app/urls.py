from django.urls import path, include

from exam3_v2.notes_app.views import home_view, add_note_view, edit_note_view, \
    delete_note_view, note_details_view, profile_view, delete_profile_and_notes_view

urlpatterns = [
    path('', home_view, name='index'),
    path('add/', add_note_view, name='add note page'),
    path('edit/<int:pk>/', edit_note_view, name='edit note page'),
    path('delete/<int:pk>/', delete_note_view, name='delete note page'),
    path('details/<int:pk>/', note_details_view, name='note details page'),
    path('profile/', profile_view, name='profile page'),
    path('profile/delete/<int:pk>', delete_profile_and_notes_view, name='delete profile page'),
]
