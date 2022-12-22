from django import forms

class PostUpdateForm(forms.Form):
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_control'}))
