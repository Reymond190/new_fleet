from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import AddDevice
from django.views.decorators.cache import cache_control
from .forms import  AddDeviceform


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def settings(request):
    l = AddDevice.objects.all()
    form = AddDeviceform
    context = {'form2':form,"device_list":l}
    if request.method == 'POST' and 'button-name2' in request.POST:
        form2 = AddDeviceform(request.POST)
        if form2.is_valid():
            print("getting inside if")
            fs = form2.save(commit=False)
            fs.user = request.user
            fs.save()
            print("save")
        messages.success(request, 'Device Added')
    return render(request,'setttings/settings.html',context)