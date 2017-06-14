from django import forms
from apps.screen.models import Prevent, Video

class PreventForm(forms.ModelForm):

    class Meta:
        model = Prevent
        fields = [
            'type',
            'item'
        ]
        labels = {
            'type':'Type',
            'item':'Item'
        }
        widgets = {
            'type' : forms.Select(attrs={'class':'form-control'}),
            'item' : forms.TextInput(attrs={'class':'form-control'})
        }

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = [
            'type',
            'url'
        ]
        labels = {
            'type':'Type',
            'url':'Url'
        }
        widgets = {
            'type' : forms.Select(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'class':'form-control'})
        }
