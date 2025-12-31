from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    # Pega o que o usuário digitou na busca (se digitou algo)
    busca = request.GET.get('busca')
    
    if busca:
        # Filtra pelo nome (icontains = contém o texto, ignorando maiúscula/minúscula)
        # OU filtra pelo lote
        produtos = Produto.objects.filter(nome__icontains=busca) | Produto.objects.filter(lote__icontains=busca)
    else:
        # Se não buscou nada, traz tudo
        produtos = Produto.objects.all()
    
    return render(request, 'core/lista_produtos.html', {'produtos': produtos})