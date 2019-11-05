from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    nome_fantasia = models.CharField(max_length=120, blank=True)
    
    ativo = models.BooleanField(default=True)
    vendedor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cadastro = models.DateField(auto_now_add=True)

    endereco = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=78, blank=True)
    cidade = models.CharField(max_length=78, blank=True)
    uf = models.CharField(max_length=8, blank=True)
    cep = models.CharField(max_length=20, blank=True)
    contato = models.CharField(max_length=78, blank=True)

    tel = models.CharField(max_length=32, blank=True)
    celular = models.CharField(max_length=32, blank=True)
    fax = models.CharField(max_length=32, blank=True)
    
    email = models.EmailField(blank=True)

    cnpj = models.CharField(max_length=32, blank=True)
    ie = models.CharField(max_length=32, blank=True)

    cpf = models.CharField(max_length=32, blank=True)
    rg = models.CharField(max_length=32, blank=True)

    observacoes = models.TextField(blank=True)

    endereco_entrega = models.CharField(max_length=200, blank=True)
    bairro_entrega = models.CharField(max_length=78, blank=True)
    cidade_entrega = models.CharField(max_length=78, blank=True)
    uf_entrega = models.CharField(max_length=8, blank=True)
    cep_entrega = models.CharField(max_length=20, blank=True)


    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
