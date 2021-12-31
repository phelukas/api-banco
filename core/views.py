from rest_framework.permissions import IsAuthenticated
from rest_framework_xml.renderers import XMLRenderer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from django.forms.models import model_to_dict
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from core import serializers
from core import models
from core import utils


class UserView(APIView):

    def get(self, request, pk=None):

        users = User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):

        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteView(APIView):
    """View que lista todos os clientes e suas informações."""

    renderer_classes = [JSONRenderer,XMLRenderer,]
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):

        try:
            return models.Cliente.objects.get(pk=pk)
        except:
            raise Http404    

    @method_decorator(cache_page(60*2))
    def get(self, request, pk=None):

        if pk:
            cliente_object = self.get_object(pk)
            serializer = serializers.ClienteSerializer(cliente_object)  
            response = serializer.data
            pessoa = models.Pessoa.objects.get(id=response["pessoa"])
            pessoa_dici = model_to_dict(pessoa)
            pessoa_dici["cpfcnpj"] = pessoa.cpfcnpj_formatado
            response["pessoa"] = pessoa_dici
            response["banco"] = models.Banco.objects.filter(id=response["banco"]).values()
            return Response(response, status=status.HTTP_200_OK)

        clientes = models.Cliente.objects.all()
        serializer = serializers.ClienteSerializer(clientes, many=True)
        data = serializer.data

        for campo in data:
            id_pessoa = campo["pessoa"]
            id_banco = campo["banco"]
            pessoa = models.Pessoa.objects.get(id=id_pessoa)

            pessoa_dici = model_to_dict(pessoa)
            pessoa_dici["cpfcnpj"] = pessoa.cpfcnpj_formatado
            campo["banco"] = models.Banco.objects.filter(id=id_banco).values()
            campo["pessoa"] = pessoa_dici

        return Response(data, status=status.HTTP_200_OK)


    def post(self, request, format=None):

        serializer_pessoa = serializers.PessoaSerializer(data=request.data)

        if serializer_pessoa.is_valid():
            pessoa = serializer_pessoa
            serializer_pessoa.save()
        else:
            return Response(serializer_pessoa.errors, status=status.HTTP_400_BAD_REQUEST)

        
        serializer_cliente = serializers.ClienteSerializer(data=request.data,context={'pessoa':pessoa.instance})

        if serializer_cliente.is_valid():
            serializer_cliente.save()
            return Response(serializer_cliente.data, status=status.HTTP_201_CREATED)
        else:
            models.Pessoa.objects.get(id=pessoa.instance.id).delete()
            return Response(serializer_cliente.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk, format=None):

        cliente_object = self.get_object(pk)

        serializer_pessoa = serializers.PessoaSerializer(cliente_object.pessoa, data=request.data)

        if serializer_pessoa.is_valid():
            pessoa = serializer_pessoa
            serializer_pessoa.save()
        else:
            return Response(serializer_pessoa.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        serializer_cliente = serializers.ClienteSerializer(cliente_object, data=request.data,context={'pessoa':pessoa.instance})

        if serializer_cliente.is_valid():
            serializer_cliente.save()
            return Response(serializer_cliente.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_cliente.errors, status=status.HTTP_400_BAD_REQUEST) 


    def patch(self, request, pk, format=None):

        cliente_object = self.get_object(pk)

        serializer_pessoa = serializers.PessoaSerializer(cliente_object.pessoa, data=request.data, partial=True)

        if serializer_pessoa.is_valid():
            pessoa = serializer_pessoa
            serializer_pessoa.save()
        else:
            return Response(serializer_pessoa.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        serializer_cliente = serializers.ClienteSerializer(cliente_object, data=request.data,context={'pessoa':pessoa.instance},partial=True)

        if serializer_cliente.is_valid():
            serializer_cliente.save()
            return Response(serializer_cliente.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_cliente.errors, status=status.HTTP_400_BAD_REQUEST)         


class BancoView(APIView):
    """View responsavel pela listagem dos bancos cadastrados"""

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):

        try:
            return models.Banco.objects.get(pk=pk)
        except:
            raise Http404

    @method_decorator(cache_page(60*2))
    def get(self, request, pk=None):

        if pk:
            banco_object = self.get_object(pk)
            serializer = serializers.BancoSerializer(banco_object)    
            return Response(serializer.data, status=status.HTTP_200_OK)


        bancos = models.Banco.objects.all()

        serializer = serializers.BancoSerializer(bancos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):

        serializer = serializers.BancoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):

        snippet = self.get_object(pk)
        serializer = serializers.BancoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def patch(self, request, pk, format=None):

        snippet = self.get_object(pk)
        serializer = serializers.BancoSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        banco_object = self.get_object(pk)

        banco_data = request.data

        data = {}

        if len(models.Cliente.objects.filter(banco=banco_object)) > 0:
            data['msg'] = "Não é possivel deletar um banco com clientes vinculado"
            return Response(data)  
        
        else:
            banco_object.delete()
            data['msg'] = "Banco deletado com sucesso"
            return Response(data)     


class SaqueView(APIView):
    """View responsavel pelo saque."""

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):

        try:
            return models.Cliente.objects.get(pk=pk)
        except:
            raise Http404


    def post(self, request, pk, format=None):

        cliente_object = self.get_object(pk)
        valor =  float(request.data["valor"])
        response = []
        data = {}

        if utils.saque(cliente_object, valor):
            data["sucess"] = "Saque realizado com sucesso"
            data["valor_sacado"] = str(valor)
            data["saldo_conta"] = float(cliente_object.saldo_total)
            response.append(data)
            return Response(data,status=status.HTTP_200_OK)

        else:
            data["error"] = "Saldo insuficiente"
            data["saldo_conta"] = str(cliente_object.saldo_total)
            response.append(data)
            return Response(data,status=status.HTTP_400_BAD_REQUEST)   


class DepositoView(APIView):
    """View responsavel pelo deposito em conta."""

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):

        try:
            return models.Cliente.objects.get(pk=pk)
        except:
            raise Http404
    

    def post(self, request, pk, format=None):

        cliente_object = self.get_object(pk)
        valor =  float(request.data["valor"])
        response = []
        data = {}

        if utils.deposito(cliente_object, valor):
            data["sucess"] = "Saque realizado com sucesso"
            data["valor_depositado"] = str(valor)
            data["saldo_conta"] = cliente_object.saldo_total
            response.append(data)
            return Response(data,status=status.HTTP_200_OK)

        else:
            data["error"] = "Verifique as informações passadas"
            response.append(data)
            return Response(data,status=status.HTTP_400_BAD_REQUEST)   
