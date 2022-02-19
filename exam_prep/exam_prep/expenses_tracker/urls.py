from django.urls import path
from .views import home_view, create_expense, edit_expense, delete_expense, \
    view_profile, edit_profile, delete_profile

urlpatterns = [
    path('', home_view, name='home page'),
    path('create/', create_expense, name='create expense page'),
    path('edit/<int:pk>/', edit_expense, name='expense edit page'),
    path('delete/<int:pk>/', delete_expense, name='expense delete page'),
    path('profile/', view_profile, name='profile page'),
    path('profile/edit/<int:pk>/', edit_profile, name='profile edit page'),
    path('profile/delete/<int:pk>/', delete_profile, name='delete profile page'),
]
