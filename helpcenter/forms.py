from .models import Helpcenter
from django import forms

class HelpCenterform(forms.ModelForm):
    class Meta:
        model = Helpcenter
        fields = ['Title','How_can_we_help_you','message','comments']


