from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import AddTicketsForm
from .models import AddTickets
from django.contrib import messages


def tickets(request):
    form3 = AddTicketsForm

    if request.method == 'POST' and 'button-name2' in request.POST:
        form3 = AddTicketsForm(request.POST)
        if form3.is_valid():
            print("getting inside if")
            fs = form3.save(commit=False)
            fs.save()
            print("save")
        messages.success(request, 'Tickets Added')

    one = AddTickets.objects.all()
    #if request.method == 'POST' and 'reymond3' in request.POST:

    context = {"form3": form3,'voot':one}

    return render(request, 'tickets/tickets.html', context)


def v1(request):
    print('hello')
    veh = request.GET['dataa']
    i = str(veh)
    a = AddTickets.objects.get(Ticket_Name=i)
    a.delete()
    print (a.Ticket_Name)
    print(veh)
    return JsonResponse(veh)


def username_exists(request):
    data = {'msg':''}
    area = request.GET['action']
    print(area[0])
    if request.method == 'GET':
        username = request.GET.get('username').lower()
        exists = True
        if exists:
            data['msg'] = username + ' already exists.'
            print(data['msg'])
        else:
            data['msg'] = username + ' does not exists.'
    return JsonResponse(data)
