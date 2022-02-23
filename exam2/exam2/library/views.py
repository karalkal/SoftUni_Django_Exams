from django.shortcuts import render, redirect

from exam2.library.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateBookForm, EditBookForm
from exam2.library.models import Profile, Book


def get_profile():
    return Profile.objects.first()


def home_view(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile page')

    else:  # if profile exists
        books = Book.objects.all()
        context = {'books': books, 'profile': profile}
        return render(request, 'home-with-profile.html', context)


def add_book_view(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateBookForm()
    return render(request, 'add-book.html', {'form': form, 'profile': profile})


def edit_book_view(request, pk):
    profile = get_profile()
    book_to_edit = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book_to_edit)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditBookForm(instance=book_to_edit)
    return render(request, 'edit-book.html',
                  {'form': form, 'book_to_edit': book_to_edit, 'profile': profile})


def delete_book_view(request, pk):
    Book.objects.get(pk=pk).delete()
    return redirect('index')


def book_details_view(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    return render(request, 'book-details.html', {'book': book, 'profile': profile})


def profile_details_view(request):
    profile = get_profile()
    return render(request, 'profile.html', {'profile': profile})


def create_profile_view(request):
    no_profile = True
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # if created successfully redirect to index -> home-with-profile

    else:  # if GET request
        form = CreateProfileForm()

    context = {'no_profile': no_profile, 'form': form}
    return render(request, 'home-no-profile.html', context)


def edit_profile_view(request):
    profile = get_profile()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'edit-profile.html', {'form': form})


def delete_profile_view(request):
    profile = get_profile()
    if request.method == 'POST':
        Book.objects.all().delete
        profile.delete()
        return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)
        return render(request, 'delete-profile.html', {'form': form})
