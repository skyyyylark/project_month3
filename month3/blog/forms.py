from django import forms
from rest_framework import serializers

from . import models


class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    hashtags = forms.CharField()


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = [
            'id',
            'image',
            'title',
            'description',
            'hashtags',
        ]

class CreateComment(forms.ModelForm):
    comment = forms.CharField(max_length=200)
    class Meta:
        fields = '__all__'
        model = models.Comment