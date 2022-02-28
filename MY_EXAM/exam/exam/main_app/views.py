from django.shortcuts import render, redirect, HttpResponse

from exam.main_app.forms import CreateProfileForm, CreateAlbumForm, DeleteAlbumForm
from exam.main_app.models import Profile, Album


# helper functions #
def get_profile():
    return Profile.objects.first()


def get_all_albums():
    return Album.objects.all()


# views #
def index_view(request):
    profile = get_profile()
    if not profile:
        return redirect("create profile page")
    else:
        albums = get_all_albums()
        return render(request, 'home-with-profile.html', {'albums': albums})


def add_album_view(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index page')
    else:
        form = CreateAlbumForm()
    return render(request, 'add-album.html',
                  {'form': form})


def edit_album_view(request, pk):
    album_to_edit = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST, instance=album_to_edit)
        if form.is_valid():
            form.save()
            return redirect('index page')
    else:
        form = CreateAlbumForm(instance=album_to_edit)
    return render(request, 'edit-album.html',
                  {'form': form,
                   'album_to_edit': album_to_edit})


def delete_album_view(request, pk):
    album_to_delete = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album_to_delete)
        form.save()
        return redirect('index page')
    else:
        form = DeleteAlbumForm(instance=album_to_delete)
    return render(request, 'delete-album.html',
                  {'form': form,
                   'album_to_delete': album_to_delete})


def album_details_view(request, pk):
    album_to_view = Album.objects.get(pk=pk)
    return render(request, 'album-details.html',
                  {'album_to_view': album_to_view})


def profile_details_view(request):
    albums_count = get_all_albums().count()
    profile = get_profile()
    return render(request, 'profile-details.html',
                  {'profile': profile,
                   'albums_count': albums_count})


def profile_create_view(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index page')
    else:
        form = CreateProfileForm()
    return render(request, 'home-no-profile.html',
                  {'no_profile': True,
                   'form': form, }
                  )


def delete_profile_view(request):
    if request.method == 'POST':
        profile = get_profile()
        albums = get_all_albums()
        profile.delete()
        albums.delete()
        return redirect('index page')
    # otherwise
    return render(request, 'profile-delete.html')
