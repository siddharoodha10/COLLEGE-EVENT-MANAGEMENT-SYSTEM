from django import forms
from evmanage.models import Event

class EventForm(form.ModelForm):
    class meta:
        model= Event
        fields = "__all__" 
       
        """all required to be in form"""

class studentForm(form.ModelForm):
    class meta:
        model= student
        fields = "__all__" 


class adminForm(form.ModelForm):
    class meta:
        model= admin
        fields = "__all__" 