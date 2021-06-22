from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


# Create your views here.

def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 10)
    page_number = request.GET.get('p')
    contatos = paginator.get_page(page_number)
    return render(request, 'contato/index.html', {
        'contatos': contatos
    })


def detalhes(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()

    return render(request, 'contato/detalhes.html', {
        'contato': contato
    })


# def detalhes(request, contato_id):
#     try:
#         contato = Contato.objects.get(id=contato_id)
#         return render(request, 'contato/detalhes.html', {
#             'contato': contato
#         })
#     except Contato.DoesNotExist as e:
#         raise Http404()

def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(
            request, messages.ERROR,
            'Campo busca não pode estar vazio.'
        )
        return redirect('index')
    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) |
        Q(telefone__icontains=termo)
    )
    # contatos = Contato.objects.order_by('-id').filter(
    #     Q(nome__icontains=termo) |
    #     Q(sobrenome__icontains=termo),
    #     mostrar=True
    # )
    paginator = Paginator(contatos, 10)
    page_number = request.GET.get('p')
    contatos = paginator.get_page(page_number)
    return render(request, 'contato/busca.html', {
        'contatos': contatos
    })
