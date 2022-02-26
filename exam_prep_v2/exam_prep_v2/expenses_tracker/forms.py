from django import forms

from exam_prep_v2.expenses_tracker.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        widgets = {
            'profile_image': forms.FileInput(
                attrs={'class': "form-file"}
            )
        }


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        self.instance.delete()  # to remove record from DB
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
