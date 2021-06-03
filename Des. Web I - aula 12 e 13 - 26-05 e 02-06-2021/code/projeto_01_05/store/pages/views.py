from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'intro':'Bem vindos a aula de Desenvolvimento Web I',
        'info':'Turma 2021-1',
        'intro2':'Mastering Django Web Dev'
    }
    return render(request, 'index.html', context=context)

def about(request):
    context = {
        'intro':'Sobre nós',
        'info':'Em construção',
    }
    return render(request, 'about.html', context=context)