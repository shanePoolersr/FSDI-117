from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['name', 'description', 'year', 'img', 'respository', 'technologies']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Projects Description'}),
            
            'description': forms.TextInput(attrs={'placeholder': 'Projects Description'}),
            
            'year': forms.NumberInput(attrs={'placeholder': 'Year'}),
            
            'img': forms.ClearableFileInput(attrs={'placeholder': 'Select an Image'}),
            
            'respository': forms.URLInput(attrs={'placeholder': 'Respositiry URL '}),
            
        
        }