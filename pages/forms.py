from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=225, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    message =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Message'}))
    
    