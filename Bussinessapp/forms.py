from Bussinessapp.models import Customer
from django import forms

#Create Your Forms here
class Query(forms.ModelForm):
    subject = forms.CharField(max_length=500)
    Message = forms.TextField()

    class Meta():
        model = Customer
        fields = ('Name','Email','Contact_no')
