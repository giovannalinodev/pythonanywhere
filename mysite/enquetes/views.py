from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pergunta, Alternativa
from django.urls import reverse


def index(request):
    lista_perguntas = Pergunta.objects.order_by('-data_pub')
    contexto = { 'lista_perguntas' : lista_perguntas}
    return render(request, 'enquetes/index.html', contexto)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, 'enquetes/detalhes.html', {'pergunta': pergunta})

def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    try:
        alt_id = request.POST['alt_id']
        alt_escolhida = pergunta.alternativa_set.get(pk=alt_id)
    except (KeyError, Alternativa.DoesNotExist):
        contexto = {
            'pergunta': pergunta, 'error': 'Você precisa selecionar uma alternativa válida!'
        }
        return render(request, 'enquetes/detalhes.html', contexto)
    else:
        alt_escolhida.quant_votos += 1
        alt_escolhida.save()
        return HttpResponseRedirect(
            reverse('enquetes:resultado', args=(pergunta.id,))
        )

    #resposta = '<h1>Votação da enquete %s<h1>' % pergunta_id
    #return HttpResponse(resposta)


def resultado(request, pergunta_id):
    resposta = '<h1>Resultado da enquete %s<h1>' % pergunta_id
    return HttpResponse(resposta)


def sobre(request):
    return HttpResponse('&copy; DSWeb/TADS/CNAT/IFRN, 2023.')

# CÓDIGO DUPLICADO INTENCIONAL PARA TESTE DO DETECTOR
def validar_usuario_acesso(request, required_permission=None):
    """
    Função para validar se o usuário tem acesso
    Esta é uma duplicação intencional para teste
    """
    if not request.user.is_authenticated:
        return False
    
    if required_permission and not request.user.has_perm(required_permission):
        return False
    
    return True

def processar_dados_formulario(request, form_data):
    """
    Processa dados do formulário com validação
    Esta é uma duplicação intencional para teste
    """
    dados_processados = {}
    
    for campo, valor in form_data.items():
        if valor and valor.strip():
            dados_processados[campo] = valor.strip()
        else:
            dados_processados[campo] = None
    
    return dados_processados

def configurar_contexto_usuario(request, dados_extras=None):
    """
    Configura contexto padrão do usuário
    Esta é uma duplicação intencional para teste
    """
    contexto = {
        'user': request.user,
        'is_authenticated': request.user.is_authenticated,
        'user_id': request.user.id if request.user.is_authenticated else None,
    }
    
    if dados_extras:
        contexto.update(dados_extras)
    
    return contexto

"""
1ª versão da visão de index
def index(request):
    lista_perguntas = Pergunta.objects.order_by('-data_pub')
    resposta = '<br/>'.join([p.texto for p in lista_perguntas])
    return HttpResponse('<h1>%s</h1>'%resposta)

2ª versão da visão de index

from django.template import loader

def index(request):
    lista_perguntas = Pergunta.objects.order_by('-data_pub')
    template = loader.get_template('enquetes/index.html') #2 estágios onde carregar objeto para a memória e renderizar
    contexto = { 'lista_perguntas' : lista_perguntas}
    return HttpResponse(template.render(contexto, request))

1ª versão detalhes

from django.http import HttpResponse, Http404

def detalhes(request, pergunta_id):
#pode gerar uma exceção#
    try:
        pergunta = Pergunta.objects.get(id=pergunta_id)
    except Pergunta.DoesNotExist:
        raise Http404('Nenhuma enquete satisfaz esse critério.')
    return render(request, 'enquetes/detalhes.html', {'pergunta': pergunta})

"""
