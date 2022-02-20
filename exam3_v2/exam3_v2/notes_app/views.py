from django.shortcuts import render, HttpResponse, redirect

from exam3_v2.notes_app.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from exam3_v2.notes_app.models import Profile, Note


def get_profile():
    return Profile.objects.first()  # returns first object in queryset or None


def get_all_notes():
    return Note.objects.all()


def get_note_by_pk(pk):
    return Note.objects.get(pk=pk)


def home_view(request):
    # return HttpResponse("It works.")
    profile = get_profile()

    if profile:
        notes = get_all_notes()
        return render(request, 'home-with-profile.html', {'notes': notes})

    else:
        hide_add_note_button = True
        hide_profile_button = True
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')

        else:
            form = CreateProfileForm()  # if GET, new form
            return render(request, 'home-no-profile.html',
                          {'form': form,
                           'hide_add_note_button': hide_add_note_button,
                           'hide_profile_button': hide_profile_button, }
                          )


def add_note_view(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        hide_add_note_button = True
        form = CreateNoteForm()
        return render(request, 'note-create.html',
                      {'form': form,
                       'hide_add_note_button': hide_add_note_button, }
                      )


def edit_note_view(request, pk):
    note_to_edit = get_note_by_pk(pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note_to_edit)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNoteForm(instance=note_to_edit)
        return render(request, 'note-edit.html',
                      {'form': form,
                       'note_to_edit': note_to_edit}
                      )


def delete_note_view(request, pk):
    note_to_delete = get_note_by_pk(pk)
    if request.method == 'POST':
        note_to_delete.delete()
        return redirect('index')
    else:
        form = DeleteNoteForm(instance=note_to_delete)
        return render(request, 'note-delete.html',
                      {'form': form,
                       'note_to_delete': note_to_delete}
                      )


def note_details_view(request, pk):
    note_to_view = get_note_by_pk(pk)
    return render(request, 'note-details.html', {'note_to_view': note_to_view})


def profile_view(request):
    profile = get_profile()
    notes_count = get_all_notes().count()
    return render(request, 'profile.html', {'profile': profile,
                                            'notes_count': notes_count})


def delete_profile_and_notes_view(request, pk):
    profile = get_profile()
    notes = get_all_notes()
    profile.delete()
    notes.delete()
    return redirect('index')
