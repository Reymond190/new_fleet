from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddTicketsForm
from .models import AddTickets
from django.contrib import messages


# def tickets(request):
#     form3 = AddTicketsForm
#
#     time2 = datetime.now()
#     if request.method == 'GET' and 'jose2' in request.GET:
#         i = AddTickets.objects.filter(id=3)
#     if request.method == 'GET' and 'reymond3' in request.GET:
#         i.delete()
#         print('oooooele')
#     if request.method == 'POST' and 'button-name2' in request.POST:
#         form3 = AddTicketsForm(request.POST)
#         if form3.is_valid():
#             print("getting inside if")
#             fs = form3.save(commit=False)
#             fs.save()
#             print("save")
#         messages.success(request, 'Tickets Added')
#
#     one = AddTickets.objects.all()
#     #if request.method == 'POST' and 'reymond3' in request.POST:
#
#     context = {"form3": form3,'voot':one}
#
#     return render(request, 'tickets/tickets.html', context)

import json
def tickets(request):
    if request.method == "POST":
        get_value = request.body
        print(get_value)
    return render(request, 'tickets/tickets.html')