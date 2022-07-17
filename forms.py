from django import forms  
from cars.models import Names  
class CarForm(forms.ModelForm):  
    class Meta:  
        model = Names
        fields = "__all__" 