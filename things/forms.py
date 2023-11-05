"""Forms of the project."""
from django import forms
from .models import Thing
# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model =Thing
        fields=['name','description','quantity']
    #name = forms.CharField(type='text',max_length=35)
    #description=forms.Textarea(widget=forms.Textarea)
    quantity=forms.NumberInput()