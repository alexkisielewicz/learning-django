from django import forms
from .models import Item


# we can render a rorm as a template variable 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "done"]
