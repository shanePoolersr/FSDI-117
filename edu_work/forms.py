from django import forms
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['entity', 'title', 'description', 'period', 'technologies']
        widgets = {
            'entity': forms.TextInput(attrs={'placeholder': 'Entity name'}),
						
			'title': forms.TextInput(attrs={'placeholder': 'Title'}),

            'description': forms.Textarea(attrs={'placeholder': 'Description'}),

            'period': forms.TextInput(attrs={'placeholder': 'month YYYY - month YYYY'}),
 
        }
