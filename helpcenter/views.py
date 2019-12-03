from django.contrib import messages
from django.shortcuts import render
from .models import Helpcenter
from .forms import HelpCenterform
# Create your views here.

def helpcenter(request):
    l = Helpcenter.objects.all()
    form = HelpCenterform
    context = {'form2': form, "help": l}
    if request.method == 'POST' and 'button-name2' in request.POST:
        form2 = HelpCenterform(request.POST)
        if form2.is_valid():
            print("getting inside if")
            fs = form2.save(commit=False)
            fs.user = request.user
            fs.save()
            print("save")
        messages.success(request, 'Message Added')
    return render(request, 'help_center/helpcenter.html',context)
