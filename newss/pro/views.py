from django.shortcuts import render
from.models import Articles
def pro_home(request):
    pro = Articles.objects.order_by('-date')
    return render(request, 'pro/pro_home.html', {'pro': pro})
