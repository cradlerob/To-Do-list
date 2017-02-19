from django import forms
from lists.models import Item,List


class ItemForm (forms.models.ModelForm):
    text = forms.CharField(max_length=120)
    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
            }),
        }


class EditItemForm(ItemForm):
    text = forms.CharField( max_length = 120 )
    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
            }),
        }

class ListForm(forms.models.ModelForm):
    name = forms.CharField( max_length = 70 ,widget=forms.TextInput(attrs={
                'placeholder': 'Enter a To-Do list tittle',}),)
    class Meta:
        model = List
        fields = ('name',)