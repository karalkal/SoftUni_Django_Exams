from django.shortcuts import render, redirect

from exam1_v2.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from exam1_v2.recipes.models import Recipe


def get_recipe(pk):
    return Recipe.objects.get(pk=pk)


def home_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def create_view(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateRecipeForm()

    return render(request, 'create.html', {'form': form})


def edit_view(request, pk):
    recipe_to_edit = get_recipe(pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe_to_edit)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditRecipeForm(instance=recipe_to_edit)

    return render(request, 'edit.html',
                  {'form': form, 'recipe_to_edit': recipe_to_edit})


def delete_view(request, pk):
    recipe_to_delete = get_recipe(pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe_to_delete)
        form.save()
        return redirect('index')
    else:
        form = DeleteRecipeForm(instance=recipe_to_delete)

    return render(request, 'delete.html',
                  {'form': form, 'recipe_to_delete': recipe_to_delete})


def details_view(request, pk):
    recipe_to_view = get_recipe(pk)
    ingredients = recipe_to_view.ingredients.split(",")
    return render(request, 'details.html',
                  {'recipe_to_view': recipe_to_view, 'ingredients': ingredients})
