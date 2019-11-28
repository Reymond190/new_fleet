from datetime import datetime

from django.shortcuts import render
from .forms import AddTicketsForm
from .models import AddTickets
from django.contrib import messages
# Create your views here.

def tickets(request):
    form3 = AddTicketsForm
    time2 = datetime.now()
    if request.method == 'POST' and 'button-name2' in request.POST:
        form3 = AddTicketsForm(request.POST)
        if form3.is_valid():
            print("getting inside if")
            fs = form3.save(commit=False)

            fs.save()
            print("save")
        messages.success(request, 'Tickets Added')

    one = AddTickets.objects.all()
    context = {"form3": form3,'voot':one}

    return render(request, 'tickets/tickets.html', context)
