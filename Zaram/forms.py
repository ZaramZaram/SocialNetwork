from django import forms
from .models import Post, PostComment

class PostUpdateForm(forms.Form):
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_control'}))

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model: PostComment
        fields = ('body')

