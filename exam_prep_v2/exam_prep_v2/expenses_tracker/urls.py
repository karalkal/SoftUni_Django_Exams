from django.urls import path

from exam_prep_v2.expenses_tracker.views import index_view, create_expense_view, edit_expense_view, delete_expense_view, \
    profile_view, create_profile_view, edit_profile_view, delete_profile_view

urlpatterns = [
    path('', index_view, name="index"),
    path('create/', create_expense_view, name="create expense"),
    path('edit/<int:pk>/', edit_expense_view, name="edit expense"),
    path('delete/<int:pk>/', delete_expense_view, name="delete expense"),
    path('profile/', profile_view, name="profile"),
    path('profile/create', create_profile_view, name="create profile"),
    path('profile/edit/', edit_profile_view, name="profile edit"),
    path('profile/delete/', delete_profile_view, name="delete profile"),
]
