from rest_framework import serializers
from core import models
import random

class BancoSerializer(serializers.ModelSerializer):

    quantidade_clientes = serializers.ReadOnlyField()
    class Meta:
        ordering = ['-created']
        model = models.Banco
        fields = '__all__'

    def create(self, validated_data):
        banco = models.Banco.objects.create(**validated_data)
        return banco
       
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.cheque_especial_inicial = validated_data.get('cheque_especial_inicial', instance.cheque_especial_inicial)
        instance.limite_inicial = validated_data.get('limite_inicial', instance.limite_inicial)
        instance.save()
        return instance


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-pk']
        model = models.Cliente
        fields = '__all__'

    def get_conta(self, banco):

        conta = random.randint(0, 9999)
        clientes = models.Cliente.objects.all()
        contas_list = list()

        if len(models.Cliente.objects.filter(banco=banco, conta=conta)) > 0:

            for cliente in clientes:
                contas_list.append(cliente.conta)

            conta = random.randint(0, 9999)
            
            i = True
            while i:
                i = False if conta not in contas_list else True
            
        return conta

    
    def create(self, validated_data):

        pessoa = self.context['pessoa']
        banco = validated_data['banco']
        senha = validated_data['senha']
        agencia = random.randint(0, 99999)
        conta = self.get_conta(validated_data['banco'])
        saldo = validated_data['saldo']
        cheque_especial = validated_data['cheque_especial']

        cliente = models.Cliente.objects.create(
            banco=banco,
            pessoa=pessoa,
            senha=senha,
            agencia=agencia,
            conta=conta,
            saldo=saldo,
            cheque_especial=cheque_especial,
        )

        return cliente

    def update(self, instance, validated_data):

        instance.senha = validated_data.get('senha', instance.senha)
        instance.save()
        return instance


class PessoaSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-created']
        model = models.Pessoa
        fields = '__all__'

    def create(self, validated_data):
        pessoa = models.Pessoa.objects.create(**validated_data)
        return pessoa


    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.sexo = validated_data.get('sexo', instance.sexo)
        instance.tipodepessoa = validated_data.get('tipodepessoa', instance.tipodepessoa)
        instance.nomefantasia = validated_data.get('nomefantasia', instance.nomefantasia)
        instance.cpfcnpj = validated_data.get('cpfcnpj', instance.cpfcnpj)
        instance.datanascimento = validated_data.get('datanascimento', instance.datanascimento)
        instance.estadocivil = validated_data.get('estadocivil', instance.estadocivil)
        instance.nacionalidade = validated_data.get('nacionalidade', instance.nacionalidade)
        instance.profissao = validated_data.get('profissao', instance.profissao)    
        instance.save()
        return instance
