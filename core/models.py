from django.db import models
from datetime import date

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    lote = models.CharField(max_length=20, help_text="Número do lote de fabricação")
    
    # Informações de Estoque
    quantidade = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=5, help_text="Quantidade mínima para alerta")
    
    # Informações Críticas (Indústria)
    data_validade = models.DateField()
    data_fabricacao = models.DateField(blank=True, null=True)
    
    # Metadados para saber quando foi criado/alterado
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} (Lote: {self.lote})"

    # Lógica simples para dizer se venceu
    @property
    def esta_vencido(self):
        if self.data_validade:
            return date.today() > self.data_validade
        return False

    @property
    def estoque_baixo(self):
        return self.quantidade <= self.estoque_minimo