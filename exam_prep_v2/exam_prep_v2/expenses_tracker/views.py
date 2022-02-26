from django.shortcuts import render, redirect

from exam_prep_v2.expenses_tracker.forms import CreateProfileForm, CreateExpenseForm, DeleteExpenseForm
from exam_prep_v2.expenses_tracker.models import Profile, Expense


# helper functions #
def get_profile():
    return Profile.objects.first()


def get_expenses():
    return Expense.objects.all()


def get_remaining_budget():
    profile = get_profile()
    expenses = get_expenses()
    return profile.budget - sum([int(x.price) for x in expenses])


# views #
def index_view(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    else:
        expenses = get_expenses()
        budget_left = get_remaining_budget()
        return render(request, 'home-with-profile.html',
                      {'profile': profile,
                       'expenses': expenses,
                       'budget_left': budget_left})


def create_expense_view(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateExpenseForm()
    return render(request, 'expense-create.html', {'form': form})


def delete_expense_view(request, pk):
    expense_to_delete = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense_to_delete)
        form.save()  # save is overwritten
        return redirect('index')
    else:
        form = DeleteExpenseForm(instance=expense_to_delete)

    return render(request, 'expense-delete.html',
                  {'form': form,
                   'expense_to_delete': expense_to_delete})


def edit_expense_view(request, pk):
    expense_to_edit = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST, instance=expense_to_edit)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateExpenseForm(instance=expense_to_edit)

    return render(request, 'expense-edit.html',
                  {'form': form,
                   'expense_to_edit': expense_to_edit})


def profile_view(request):
    profile = get_profile()
    expenses_count = get_expenses().count()
    budget_left = get_remaining_budget()

    return render(request, 'profile.html',
                  {'profile': profile,
                   'expenses_count': expenses_count,
                   'budget_left': budget_left, })


def create_profile_view(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()
    return render(request, 'home-no-profile.html',
                  {'no_profile': True,
                   'form': form, }
                  )


def edit_profile_view(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm(instance=profile)
    return render(request, 'profile-edit.html',
                  {'profile': profile,  # not needed as we don't use its pk or anything else, we just edit first profile
                   'form': form, }
                  )


def delete_profile_view(request):
    profile = get_profile()
    expenses = get_expenses()
    profile.delete()
    expenses.delete()
    return redirect('index')
