from django.shortcuts import render

# Create your views here.

def helpcenter(request):
    return render(request, 'help_center/helpcenter.html')