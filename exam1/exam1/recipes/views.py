from django.shortcuts import render, redirect

from exam1.recipes.forms import CreateRecipeForm, UpdateRecipeForm, DeleteRecipeForm
from exam1.recipes.models import Recipe


def home_view(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'all_recipes': all_recipes})


def create_recipe_view(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateRecipeForm()
    return render(request, 'create.html', {'form': form})


def edit_recipe_view(request, pk):
    recipe_to_edit = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateRecipeForm(request.POST, instance=recipe_to_edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateRecipeForm(instance=recipe_to_edit)
    return render(request, 'edit.html',
                  {
                      'form': form, 'recipe_to_edit': recipe_to_edit
                  })


def delete_recipe_view(request, pk):
    recipe_to_delete = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe_to_delete.delete()
        return redirect('home')
    else:
        form = DeleteRecipeForm(instance=recipe_to_delete)
    return render(request, 'delete.html',
                  {
                      'form': form, 'recipe_to_delete': recipe_to_delete
                  })


def recipe_details_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe_ingredients = recipe.ingredients.split(",")
    context = {
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients,
    }
    return render(request, 'details.html', context)