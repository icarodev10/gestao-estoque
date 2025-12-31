from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lote', 'quantidade', 'data_validade', 'status_validade')

    list_filter = ('categoria', 'data_validade')

    search_fields = ('nome', 'lote')
    
    # Mostra um ícone se estiver vencido
    def status_validade(self, obj):
        if obj.esta_vencido:
            return "❌ VENCIDO"
        return "✅ OK"