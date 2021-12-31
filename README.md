# zipbank-backend--challenge
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/devsuperior/sds1-wmazoni/blob/master/LICENSE) 

# Sobre o projeto

Essa é uam simples api de um sistema bancario com dados fictício.

## Intalação
Utilizando Docker juntamente com o docker-compose você vai ter o projeto intalado e rodando na porta 8000.
Depois de git clone entre no diretorio raiz do projeto e execute **docker-compose up**.

# REST API
A api utiliza arquitetura rest.

## Lista de clientes

### Request

`GET /api/cliente/`

     curl http://localhost:8000/api/cliente/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2
    
    {
    "agencia": "10340",
    "banco": [
        {
            "cheque_especial_inicial": 2000.0,
            "codigo": 1,
            "id": 1,
            "limite_inicial": 1000.0,
            "nome": "PLbanck"
        }
    ],
    "cheque_especial": 1000.0,
    "conta": "98329",
    "data_cadastro": "2000-06-19",
    "id": 1,
    "pessoa": {
        "cpfcnpj": "***59407***",
        "datanascimento": "1997-08-17",
        "estadocivil": "solteiro",
        "id": 1,
        "nacionalidade": "brasileiro",
        "nome": "Pedro Lucas Teixeira da Silva",
        "nomefantasia": "",
        "profissao": "programador",
        "sexo": "masculino",
        "tipodepessoa": "fisica"
    },
    "saldo": 10000.0,
    "senha": "admin2021"
    }



## Lista de bancos

### Request

`GET /api/banco/`

     curl http://localhost:8000/api/banco/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2
    
    {
    "cheque_especial_inicial": 2000.0,
    "codigo": 1,
    "id": 1,
    "limite_inicial": 1000.0,
    "nome": "PLbanck",
    "quantidade_clientes": 3
    }



## Buscar cliente por ID

### Request

`GET /api/cliente/id`

     curl http://localhost:8000/api/cliente/ID
     
     
## Criar cliente

### Request

`POST /api/cliente/`

     curl -X POST http://localhost:8000/api/cliente/ \
     --form 'nome="Maria Luiza"' \
     --form 'sexo="f"' \
     --form 'tipodepessoa="f"' \
     --form 'nomefantasia=""' \
     --form 'cpfcnpj="02884762083"' \
     --form 'datanascimento="1997-08-17"' \
     --form 'estadocivil="casado"' \
     --form 'nacionalidade="brasileiro"' \
     --form 'profissao="programador"' \
     --form 'banco=1' \
     --form 'senha="sourcecode"' \
     --form 'saldo=1000' \
     --form 'cheque_especial=1233' \


## Criar banco

### Request

`POST /api/banco/`

     curl -X POST http://localhost:8000/api/banco/ \
     --form 'codigo=7' \
     --form 'nome="SofiaBank"' \
     --form 'cheque_especial_inicial=10000' \
     --form 'limite_inicial=50000' \


## Deposito

### Request

`POST /api/deposito/{ID DA CONTA}/`

     curl -X POST http://localhost:8000/api/deposito/{ID DA CONTA}/ \
     --form 'valor=1000' \


## Saque

### Request

`POST /api/saque/{ID DA CONTA}/`

     curl -X POST http://localhost:8000/api/saque/{ID DA CONTA}/ \
     --form 'valor=1000' \


     
