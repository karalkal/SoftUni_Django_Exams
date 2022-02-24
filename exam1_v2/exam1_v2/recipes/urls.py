from django.urls import path

from exam1_v2.recipes.views import home_view, create_view, edit_view, delete_view, details_view

# from ..recipes.views import home_view, create_view, edit_view, delete_view, details_view

urlpatterns = [
    path('', home_view, name='index'),
    path('create', create_view, name='create recipe page'),
    path('edit/<int:pk>', edit_view, name='edit recipe page'),
    path('delete/<int:pk>', delete_view, name='delete recipe page'),
    path('details/<int:pk>', details_view, name='recipe details page'),
]
