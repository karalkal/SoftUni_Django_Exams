from django.shortcuts import render, redirect

from exam_prep.expenses_tracker.forms import CreateProfileForm, CreateExpenseForm, UpdateExpenseForm, DeleteExpenseForm, \
    UpdateProfileForm, DeleteProfileForm
from exam_prep.expenses_tracker.models import Profile, Expense


def get_profile():
    if Profile.objects.all():
        profile = Profile.objects.all()[0]
        return profile
    return None


def home_view(request):
    profile = get_profile()
    if not profile:
        no_profile = True
        if request.method == 'POST':
            form = CreateProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home page')
        else:
            form = CreateProfileForm()
        return render(request,
                      'home-no-profile.html',
                      {'form': form, 'no_profile': no_profile})

    # if a profile exists
    else:
        initial_budget = profile.budget
        expenses = Expense.objects.all()
        total_expenses = sum([ex.price for ex in expenses])
        # profile.budget -= total_expenses
        budget_left = initial_budget - total_expenses
        context = {
            'initial_budget': initial_budget,
            'expenses': expenses,
            'profile': profile,
            'budget_left': budget_left,
        }
        return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateExpenseForm()
    return render(request, 'expense-create.html',
                  {'form': form})


def edit_expense(request, pk):
    expense_to_edit = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateExpenseForm(request.POST, instance=expense_to_edit)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = UpdateExpenseForm(instance=expense_to_edit)
    return render(request, 'expense-edit.html',
                  {'form': form, 'expense_to_edit': expense_to_edit})


def delete_expense(request, pk):
    expense_to_delete = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        expense_to_delete.delete()
        return redirect('home page')
    else:
        form = DeleteExpenseForm(instance=expense_to_delete)
    return render(request, 'expense-delete.html',
                  {'form': form, 'expense_to_delete': expense_to_delete})


def view_profile(request):
    profile = get_profile()
    number_of_items = len(Expense.objects.all())
    budget_left = profile.budget - sum([ex.price for ex in Expense.objects.all()])

    return render(request, 'profile.html',
                  {'profile': profile,
                   'number_of_items': number_of_items,
                   'budget_left': budget_left, })


def edit_profile(request, pk):
    profile_to_edit = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile_to_edit, )
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = UpdateProfileForm(instance=profile_to_edit)
    return render(request, 'profile-edit.html',
                  {'form': form, 'profile_to_edit': profile_to_edit})


def delete_profile(request, pk):
    profile_to_delete = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        profile_to_delete.delete()
        Expense.objects.all().delete()
        return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile_to_delete)
    return render(request, 'profile-delete.html',
                  {'form': form, 'profile_to_delete': profile_to_delete})
