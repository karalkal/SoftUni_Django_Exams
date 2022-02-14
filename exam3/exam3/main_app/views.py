from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from exam3.main_app.forms import CreateNoteForm, EditNoteForm, DeleteNoteForm, CreateProfileForm
from exam3.main_app.models import Profile, Note


def home_view(request):
    profiles = Profile.objects.all()
    hide_add_note_button, hide_profile_button = True, True

    if not profiles:
        if request.method == 'POST':
            create_profile_form = CreateProfileForm(request.POST)
            if create_profile_form.is_valid():
                create_profile_form.save()
                return redirect('home')

        else:
            create_profile_form = CreateProfileForm()

        context = {
            "hide_add_note_button": hide_add_note_button,
            "hide_profile_button": hide_profile_button,
            "create_profile_form": create_profile_form
        }
        # if GET or invalid data
        return render(request, 'main_app/home-no-profile.html', context)

    else:
        notes = Note.objects.all()
        return render(request,
                      'main_app/home-with-profile.html',
                      {'notes': notes})


def add_note_view(request):
    hide_add_note_button = True
    if request.method == 'POST':
        add_note_form = CreateNoteForm(request.POST)
        if add_note_form.is_valid():
            add_note_form.save()
            return redirect('home')
    else:
        add_note_form = CreateNoteForm()

    context = {
        'add_note_form': add_note_form,
        'hide_add_note_button': hide_add_note_button
    }
    return render(request, 'main_app/note-create.html', context)


def edit_note_view(request, pk):
    note_to_edit = Note.objects.get(pk=pk)
    if request.method == 'POST':
        edit_note_form = EditNoteForm(request.POST, instance=note_to_edit)
        if edit_note_form.is_valid():
            edit_note_form.save()
            return redirect('home')
    else:
        edit_note_form = EditNoteForm(instance=note_to_edit)

    context = {
        'edit_note_form': edit_note_form,
        'note_to_edit': note_to_edit
    }
    return render(request, 'main_app/note-edit.html', context)


def delete_note_view(request, pk):
    note_to_delete = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note_to_delete.delete()
        return redirect('home')
    else:
        delete_note_form = DeleteNoteForm(instance=note_to_delete)

    context = {
        'delete_note_form': delete_note_form,
        'note_to_delete': note_to_delete
    }
    return render(request, 'main_app/note-delete.html', context)


def note_details_view(request, pk):
    searched_note = Note.objects.get(pk=pk)
    context = {
        'searched_note': searched_note
    }
    return render(request, 'main_app/note-details.html', context)


def profile_view(request):
    profile = Profile.objects.all()[0]  # since we don't have actual profiles created we just get the first one
    context = {
        'profile': profile,
        'notes_count': len(Note.objects.all())
    }
    return render(request, 'main_app/profile.html', context)


def delete_profile_view(request):
    Profile.objects.all().delete()
    Note.objects.all().delete()
    return redirect('home')
