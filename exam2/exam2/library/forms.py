from django import forms

from exam2.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': "First Name",
            'last_name': "Last name",
            'image_url': "Image URL",
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': "First Name",
                       }),

            'last_name': forms.TextInput(
                attrs={'placeholder': "Last Name",
                       }),

            'image_url': forms.URLInput(
                attrs={'placeholder': "URL",
                       }),
        }


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': "First Name",
            'last_name': "Last name",
            'image_url': "Image URL",
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': "First Name",
                       }),

            'last_name': forms.TextInput(
                attrs={'placeholder': "Last Name",
                       }),

            'image_url': forms.URLInput(
                attrs={'placeholder': "URL",
                       }),
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Profile
        fields = '__all__'


class CreateBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'first_name': "First Name",
            'last_name': "Last name",
            'image_url': "Image URL",
        }


class EditBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    class Meta:
        model = Book
        fields = '__all__'
