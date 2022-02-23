from django.urls import path

from exam2.library.views import home_view, add_book_view, edit_book_view, delete_book_view, book_details_view, \
    profile_details_view, create_profile_view,  edit_profile_view, delete_profile_view

urlpatterns = [
    path('', home_view, name='index'),
    path('add/', add_book_view, name='add book page'),
    path('edit/<int:pk>', edit_book_view, name='edit book page'),
    path('delete/<int:pk>', delete_book_view, name='delete book page'),
    path('details/<int:pk>', book_details_view, name='book details page'),
    path('profile/', profile_details_view, name='profile page'),
    path('profile/create/', create_profile_view, name='create profile page'),
    path('profile/edit/', edit_profile_view, name='edit profile page'),
    path('profile/delete/', delete_profile_view, name='delete profile page'),
]
