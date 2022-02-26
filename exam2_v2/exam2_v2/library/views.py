from django.shortcuts import render, redirect

from exam2_v2.library.forms import CreateProfileForm, CreateBookForm, DeleteProfileForm
from exam2_v2.library.models import Profile, Book


def find_profile():
    return Profile.objects.first()


def index_view(request):
    if not find_profile():
        return redirect('create profile page')
    # else
    books = Book.objects.all()
    return render(request, 'home-with-profile.html',
                  {'books': books, 'profile': find_profile()})


def create_profile_view(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()
    return render(request, 'home-no-profile.html', {'form': form, 'no_profile': True})


def add_book_view(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateBookForm()
    return render(request, 'add-book.html', {'form': form})


def edit_book_view(request, pk):
    book_to_edit = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateBookForm(request.POST, instance=book_to_edit)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateBookForm(instance=book_to_edit)
    return render(request, 'edit-book.html',
                  {'form': form,
                   'book_to_edit': book_to_edit, })


def delete_book_view(request, pk):
    Book.objects.get(pk=pk).delete()
    return redirect('index')


def book_details_view(request, pk):
    book_to_show = Book.objects.get(pk=pk)
    return render(request, 'book-details.html', {'book_to_show': book_to_show})


def profile_details_view(request):
    return render(request, 'profile.html', {'profile': find_profile()})


def edit_profile_view(request):
    profile_to_edit = find_profile()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, instance=profile_to_edit)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm(instance=profile_to_edit)
    return render(request, 'edit-profile.html', {'form': form})


def delete_profile_view(request):
    profile_to_delete = find_profile()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile_to_delete)
        profile_to_delete.delete()
        Book.objects.all().delete()
        return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile_to_delete)
        return render(request, 'delete-profile.html', {'form': form})
