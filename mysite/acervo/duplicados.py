from django.shortcuts import render, redirect
from .models import Item, Livro, Contato, Emprestimo

def get_user_items(user):
    """Retorna os itens de um usuário."""
    lista_itens = Item.objects.filter(user=user).order_by('nome')
    lista_livros = Livro.objects.filter(user=user).order_by('titulo')
    lista_contatos = Contato.objects.filter(user=user).order_by('nome_cont')
    lista_emp = Emprestimo.objects.filter(user=user, data_dev=None)
    
    emprestimos_cadastrados = lista_emp.count() > 0
    
    return {
        'lista_itens': lista_itens,
        'lista_livros': lista_livros,
        'lista_contatos': lista_contatos,
        'lista_emp': lista_emp,
        'emprestimos_cadastrados': emprestimos_cadastrados
    }

def get_user_collection(user):
    """Função duplicada que retorna as coleções de um usuário."""
    lista_itens = Item.objects.filter(user=user).order_by('nome')
    lista_livros = Livro.objects.filter(user=user).order_by('titulo')
    lista_contatos = Contato.objects.filter(user=user).order_by('nome_cont')
    lista_emp = Emprestimo.objects.filter(user=user, data_dev=None)
    
    emprestimos_cadastrados = lista_emp.count() > 0
    
    return {
        'lista_itens': lista_itens,
        'lista_livros': lista_livros,
        'lista_contatos': lista_contatos,
        'lista_emp': lista_emp,
        'emprestimos_cadastrados': emprestimos_cadastrados
    }

def create_item(request):
    """Cria um novo item."""
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    
    if not nome or not descricao:
        return False
    
    item = Item.objects.create(
        nome=nome,
        descricao=descricao,
        emprestado=False,
        user=request.user
    )
    item.save()
    return True

def create_new_item(request):
    """Função duplicada que cria um novo item."""
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    
    if not nome or not descricao:
        return False
    
    item = Item.objects.create(
        nome=nome,
        descricao=descricao,
        emprestado=False,
        user=request.user
    )
    item.save()
    return True