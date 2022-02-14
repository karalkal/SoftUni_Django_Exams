from django import forms
from .models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Note
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(attrs={"disabled": "disabled"}),
        #     'content': forms.Textarea(attrs={"disabled": "disabled"}),
        #     'image_url': forms.URLInput(attrs={"disabled": "disabled"})
        # }
