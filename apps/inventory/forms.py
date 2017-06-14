from django import forms
from apps.inventory.models import Group, State, Location, Item, Movement

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = [
            'title'
        ]
        labels = {
            'title':'Title'
        }
        widgets = {
            'title' :forms.TextInput(attrs={'class':'form-control'}),
        }

class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = [
            'title'
        ]
        labels = {
            'title':'Title'
        }
        widgets = {
            'title' :forms.TextInput(attrs={'class':'form-control'}),
        }

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = [
            'title'
        ]
        labels = {
            'title':'Title'
        }
        widgets = {
            'title' :forms.TextInput(attrs={'class':'form-control'}),
        }

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = [
            'title'
        ]
        labels = {
            'title':'Title'
        }
        widgets = {
            'title' :forms.TextInput(attrs={'class':'form-control'}),
        }

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = [
            'code',
            'description',
            'group'
        ]
        labels = {
            'code' : 'Code',
            'description': 'Description',
            'group': 'Group',
        }
        widgets = {
            'code' :forms.TextInput(attrs={'class':'form-control'}),
            'description' :forms.TextInput(attrs={'class':'form-control'}),
            'group' :forms.Select(attrs={'class':'form-control'}),
        }

class MovementForm(forms.ModelForm):

    class Meta:
        model = Movement
        fields = [
            'code',
            'state',
            'location',
            'stock'
        ]
        labels = {
            'code' : 'Code',
            'state': 'State',
            'location': 'Location',
            'stock': 'Stock'
        }
        widgets = {
            'code' :forms.Select(attrs={'class':'form-control'}),
            'state' :forms.Select(attrs={'class':'form-control'}),
            'location' :forms.Select(attrs={'class':'form-control'}),
            'stock' :forms.TextInput(attrs={'class':'form-control'}),
        }