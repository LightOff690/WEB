from django.shortcuts import render

def pro_home(request):
    return render(request, 'pro/pro_home.html')