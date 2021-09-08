from django import forms

class FormContact(forms.Form):
    name = forms.CharField(label="Name", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Email", required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class':'form-control'}))
