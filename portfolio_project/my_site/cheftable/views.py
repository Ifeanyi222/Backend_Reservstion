from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import LogForm


# Create your views here.

def formview(request):
    form = LogForm()
    if request.method=='POST':
        form=LogForm(request.POST)
        if form.is_valid():
            form.save()
    context= {"form" : form}
    return render(request, "home.html", context)



