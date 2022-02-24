from django import forms

from exam1_v2.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    class Meta:
        model = Recipe
        fields = '__all__'
        # labels = {'time': 'Time (Minutes)'} # either this or verbose_name in model


class EditRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

        for (_, field) in self.fields.items():  # Fields are not editable
            field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):  # Overwrites save() method
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'
