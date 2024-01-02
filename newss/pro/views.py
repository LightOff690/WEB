from django.shortcuts import render, redirect
from.models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView,UpdateView, DeleteView

def pro_home(request):
    pro = Articles.objects.order_by('-date')
    return render(request, 'pro/pro_home.html', {'pro': pro})

class ProDetailView(DetailView):
    model = Articles
    template_name = 'pro/details_view.html'
    context_object_name = 'article'
class ProUpdateView(UpdateView):
    model = Articles
    template_name = 'pro/pro_create.html'
    from_class = ArticlesForm

class ProDeleteView(DeleteView):
    model = Articles
    success_url = '/pro'
    template_name = 'pro/pro_delete.html'
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
