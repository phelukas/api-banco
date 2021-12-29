from django.db import models
from django.utils.translation import gettext_lazy as _
import random


class Banco(models.Model):
    """Model que guarda todas informações sobre a banco."""

    nome = models.CharField("Nome do banco", max_length=200, null=False, blank=False)
    codigo = models.IntegerField("Codigo Bancario",null=False, blank=False, unique=True)
    cheque_especial_inicial = models.FloatField("Limite Especial Inicial", null=False, blank=False)
    limite_inicial = models.FloatField("Limite Inicial", null=False, blank=False)

    class Meta:
        verbose_name = _("Banco")
        verbose_name_plural = _("Bancos")

    def __str__(self):
        return self.nome

    def quantidade_clientes(self):
        clientes = Cliente.objects.filter(banco=self).count()
        return clientes


class Pessoa(models.Model):
    """Model que guarda todas informações de uma pessoa no sistema"""
    
    nome = models.CharField("Nome", max_length=200, null=False, blank=False)
    sexo = models.CharField("Sexo", max_length=100, null=True, blank=True)
    tipodepessoa = models.CharField("Pessoa Fisica ou Juridica", max_length=30, null=False, blank=False)
    nomefantasia = models.CharField("Nome Fantasia da Empresa", max_length=255, null=True, blank=True)
    cpfcnpj = models.CharField("CPF ou CNPJ", max_length=15, null=False, blank=False, unique=True)
    datanascimento = models.DateField("Data de Nasciemnto",  null=False, blank=False)
    estadocivil = models.CharField("Estado Civil", max_length=30, blank=True, null=True)
    nacionalidade = models.CharField("Nacionalidade", max_length=100, blank=True, null=True)
    profissao = models.CharField("Profissão", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Pessoa")
        verbose_name_plural = _("Pessoas")

    def __str__(self):
        return self.nome

    @property
    def cpfcnpj_formatado(self):
        cpfcnpj_formatado = self.cpfcnpj
        cpfcnpj = list(self.cpfcnpj)
        cpfcnpj[-3:] = "***"
        cpfcnpj[:3] = "***"
        cpfcnpj_formatado = "".join(cpfcnpj)
        return cpfcnpj_formatado



class Cliente(models.Model):
    """Model que guarda todas informações e alguns calculos do cliente."""

    banco = models.ForeignKey("Banco", null=True, on_delete=models.SET_NULL)
    pessoa = models.ForeignKey("Pessoa", null=True, on_delete=models.SET_NULL)
    senha = models.CharField(max_length=100, null=False, blank=False)
    agencia = models.CharField("Agencia",max_length=100, null=False, blank=True)
    conta = models.CharField("Conta", max_length=100, null=False, blank=True)
    saldo = models.FloatField("Saldo", null=False, blank=False, default=0)
    cheque_especial = models.FloatField("Cheque Especial", null=False, blank=False, default=0)
    data_cadastro = models.DateField("Data de Cadastro",auto_now_add=True)
    
    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")
        ordering = (
            'banco',
            'pessoa',
            'senha',
            'agencia',
            'conta',
            'saldo',
            'cheque_especial',
            'data_cadastro',              
        )

    def __str__(self):
        return self.pessoa.nome

    @property
    def saldo_total(self):
        saldo_total = self.saldo + self.cheque_especial
        return saldo_total
        