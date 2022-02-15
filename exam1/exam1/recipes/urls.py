from django.urls import path

from .views import home_view, create_recipe_view, \
    edit_recipe_view, delete_recipe_view, recipe_details_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_recipe_view, name='create recipe page'),
    path('edit/<int:pk>/', edit_recipe_view, name='edit recipe page'),
    path('delete/<int:pk>/', delete_recipe_view, name='delete recipe page'),
    path('details/<int:pk>/', recipe_details_view, name='recipe details page'),
]
