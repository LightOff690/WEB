from django.shortcuts import render, redirect
from.models import Articles
from .forms import ArticlesForm
def pro_home(request):
    pro = Articles.objects.order_by('-date')
    return render(request, 'pro/pro_home.html', {'pro': pro})

def pro_create(request):
    error = ''
    if request.method =='POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='Форма была неверной'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'pro/pro_create.html', data)
