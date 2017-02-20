from django import forms
from lists.models import Item,List


class ItemForm (forms.models.ModelForm):
    text_item = forms.CharField( max_length = 120 ,widget=forms.TextInput(attrs={
                'placeholder': 'Enter a new item',}),)
    class Meta:
        model = Item
        fields = ('text_item','list')
        exclude=('list',)


class EditItemForm(ItemForm):
    text_item = forms.CharField( max_length = 120)
    class Meta:
        model = Item
        fields = ('text_item','list')

        exclude=('list',)


class ListForm(forms.models.ModelForm):
    name = forms.CharField( max_length = 70 ,widget=forms.TextInput(attrs={
                'placeholder': 'Enter a To-Do list tittle',}),)
    class Meta:
        model = List
        fields = ('name',)