from decimal import Decimal
from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=64)
    ean = models.CharField(max_length=40, blank=True)
    caixa_grande = models.IntegerField(blank=True, null=True)
    caixa_pequena = models.IntegerField(blank=True, null=True)
    ncm = models.CharField(max_length=20, blank=True)
    ii = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    ativo = models.BooleanField(default=True)
    
    origem = models.CharField(max_length=78, blank=True)
    cest = models.CharField(max_length=40, blank=True)
    
    icms = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    ipi = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))

    preco_padrao = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    observacoes = models.TextField(blank=True)
    

    class Meta:
        ordering = ['codigo']

    def __str__(self):
        return f"{self.codigo} {self.nome}"
