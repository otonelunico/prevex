from django import forms
from apps.binnacle.models import Working, Workstation, Accident, Area, Type_Accident

class WorkstationForm(forms.ModelForm):

    class Meta:
        model = Workstation
        fields = [
            'title',
            'detail'
        ]
        labels = {
            'title':'Title',
            'detail':'Detail'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'detail' : forms.TextInput(attrs={'class':'form-control'})
        }

class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = [
            'title',
            'detail'
        ]
        labels = {
            'title':'Title',
            'detail':'Detail'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'detail' : forms.TextInput(attrs={'class':'form-control'})
        }

class Type_AccidentForm(forms.ModelForm):

    class Meta:
        model = Type_Accident
        fields = [
            'title',
            'detail'
        ]
        labels = {
            'title':'Title',
            'detail':'Detail'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'detail' : forms.TextInput(attrs={'class':'form-control'})
        }

class WorkingForm(forms.ModelForm):

    class Meta:
        model = Working
        fields = [
            'name',
            'workstation',
            'area'
        ]
        labels = {
            'name': 'Name',
            'workstation': 'Workstation',
            'area': 'Area'
        }
        widgets = {
            'name' :forms.TextInput(attrs={'class':'form-control'}),
            'workstation' :forms.Select(attrs={'class':'form-control'}),
            'area' :forms.Select(attrs={'class':'form-control'})
        }


class AccidentForm(forms.ModelForm):

    class Meta:
        model = Accident
        fields = [
            'working',
            'year',
            'date',
            'hour',
            'type',
            'description',
            'observation',
            'area',
            'workstation',
            'repose'
        ]
        labels = {
            'working': 'Working',
            'year': 'Year',
            'date': 'Date',
            'hour': 'Hour',
            'type': 'Type',
            'description': 'Description',
            'observation': 'Observation',
            'area': 'Area',
            'workstation': 'Workstation',
            'repose':'Repose'
        }
        widgets = {
            'working' :forms.Select(attrs={'class':'form-control'}),
            'year' :forms.TextInput(attrs={'class':'form-control'}),
            'date' :forms.TextInput(attrs={'class':'form-control'}),
            'hour' :forms.TextInput(attrs={'class':'form-control'}),
            'type' :forms.Select(attrs={'class':'form-control'}),
            'description' :forms.Textarea(attrs={'class':'form-control'}),
            'observation' :forms.TextInput(attrs={'class':'form-control'}),
            'area' :forms.Select(attrs={'class':'form-control'}),
            'workstation' :forms.Select(attrs={'class':'form-control'}),
            'repose' :forms.TextInput(attrs={'class':'form-control'}),
        }

