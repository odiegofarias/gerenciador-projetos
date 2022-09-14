from django.shortcuts import render
from .models import Projeto



def index(request):
    projetos = Projeto.objects.all()

    return render(
        request,
        'gerenciador/index.html', {
        'projetos': projetos,
        })

