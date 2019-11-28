from .models import AddTickets
from django import forms

class AddTicketsForm(forms.ModelForm):
    class Meta:
        model = AddTickets
        fields = ['Ticket_Name', 'Description','priority']