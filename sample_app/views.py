from django.shortcuts import render



def home(request):
    return render(request,'sample_app/home.html')