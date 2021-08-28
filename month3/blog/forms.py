from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    hashtags = forms.CharField()

