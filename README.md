# zipbank-backend--challenge
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/devsuperior/sds1-wmazoni/blob/master/LICENSE) 

# Sobre o projeto

Essa é uam simples api de um sistema bancario com dados fictício.

## Intalação
Utilizando Docker juntamente com o docker-compose você vai ter o projeto intalado e rodando na porta 8000.
Depois de git clone entre no diretorio raiz do projeto e execute **docker-compose up**.

# REST API
A api utiliza arquitetura rest.

# autenticação JWT
A api utiliza o metodo de autentificação no formato JWT emtão é preciso que você crie um usuario para acesso e gere o token de autentificação para as requests. O token tem validade de 24 horas, depois você precisa gerar um novo.

#### Solicitando tokens de acesso
Para solicitar os tokens de acesso, primeiro você precisa já ter criado um usuario e depois você precisa fazer o request **POST** para http://127.0.0.1:8000/api/token/ passando o username e o password.

`POST /api/token/`

     curl -X POST "http://127.0.0.1:8000/api/user/" \
     --form 'username="pedrolucas"' \
     --form 'first_name="pedro"' \
     --form 'last_name="lucas"' \
     --form 'email="pedrolucas@gmail.com"' \
     --form 'password="pedro"' \   

### Response
     {
          "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjU5LCJqdGkiOiIyYmQ1NjI3MmIzYjI0YjNmOGI1MjJlNThjMzdjMTdlMSIsInVzZXJfaWQiOjF9.D92tTuVi_YcNkJtiLGHtcn6tBcxLCBxz9FKD3qzhUg8",
          "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTMxMDM1OSwianRpIjoiMjk2ZDc1ZDA3Nzc2NDE0ZjkxYjhiOTY4MzI4NGRmOTUiLCJ1c2VyX2lkIjoxfQ.rA-mnGRg71NEW_ga0sJoaMODS5ABjE5HnxJDb0F8xAo"
     }


## Criar um cliente

### Request

`POST /api/user/`

     curl -X POST "http://127.0.0.1:8000/api/user/" -H "accept: application/json" -H "Authorization: Bearer {access token}" -i \
     --form 'username="pedrolucas"' \
     --form 'first_name="pedro"' \
     --form 'last_name="lucas"' \
     --form 'email="pedrolucas@gmail.com"' \
     --form 'password="pedrolucas"' \ 

## Lista de clientes

### Request

`GET /api/cliente/`

     curl "http://localhost:8000/api/cliente/" -H "accept: application/json" -H "Authorization: Bearer {access token}" -i

### Response
    
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

     curl "http://localhost:8000/api/banco/" -H "accept: application/json" -H "Authorization: Bearer {access token}" -i

### Response
    
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

     curl "http://localhost:8000/api/cliente/ID/" -H "accept: application/json" -H "Authorization: Bearer {access token}" -i
     
     
## Criar cliente

### Request

`POST /api/cliente/`

     curl -X POST "http://localhost:8000/api/cliente/" -H "accept: application/json" -H "Authorization: Bearer {access token}" -i \
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

     curl -X POST "http://localhost:8000/api/banco/" -H "accept: application/json" -H "Authorization: Bearer {access token}" -i \
     --form 'codigo=7' \
     --form 'nome="SofiaBank"' \
     --form 'cheque_especial_inicial=10000' \
     --form 'limite_inicial=50000' \


## Deletar banco

### Request

`DELETE /api/banco/{ID DA CONTA}`

     curl DELETE http://localhost:8000/api/banco/{ID DA CONTA} -H "accept: application/json" -H "Authorization: Bearer {access token}" -i \

## Deposito

### Request

`POST /api/deposito/{ID DA CONTA}/`

     curl -X POST http://localhost:8000/api/deposito/{ID DA CONTA}/ -H "accept: application/json" -H "Authorization: Bearer {access token}" -i \
     --form 'valor=1000' \


## Saque

### Request

`POST /api/saque/{ID DA CONTA}/`

     curl -X POST http://localhost:8000/api/saque/{ID DA CONTA}/ -H "accept: application/json" -H "Authorization: Bearer {access token}" -i \
     --form 'valor=1000' \


     
