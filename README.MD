# CRUD com FastAPI e Docker

Este é um projeto simples de CRUD (Create, Read, Update, Delete) utilizando FastAPI como framework web e Docker para containerização. O projeto utiliza um banco de dados SQLite para armazenar os dados.

## Estrutura do Projeto

crud-app/
│
├── app/
│ ├── main.py # Código da aplicação FastAPI
│ ├── requirements.txt # Dependências do projeto
│
├── Dockerfile # Instruções para construir a imagem Docker
├── docker-compose.yml # Configuração do Docker Compose

dsconfig


## Pré-requisitos

- [Docker](https://www.docker.com/get-started) instalado na sua máquina.

## Configuração do Ambiente

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/crud-app.git
   cd crud-app
Construa e inicie os contêineres:

bash

docker-compose up --build
A aplicação estará rodando em http://localhost:8000.

Endpoints da API
A API possui os seguintes endpoints:

Criar um item

Método: POST
URL: /items/
Corpo:
json

{
  "name": "Nome do Item"
}
Ler todos os itens

Método: GET
URL: /items/
Atualizar um item

Método: PUT
URL: /items/{item_id}
Corpo:
json

{
  "name": "Nome Atualizado"
}
Deletar um item

Método: DELETE
URL: /items/{item_id}
Documentação da API