# Documentação da Aplicação

## Sobre
Este projeto tem como objetivo importar dados de produtos da API externa FakeStore para um banco de dados SQLite usando SQLAlchemy e expor esses dados através de uma API RESTful construída com Flask. A execução do projeto será feita tanto em um ambiente virtual (virtualenv) quanto em um contêiner Docker.

## Pré-requisitos
- Python 3.6 ou superior
- Docker
- Virtualenv

## Configuração do Ambiente
Clone o repositório:
`git clone <URL do repositório>`
`cd <Nome do repositório>`

## Crie o ambiente virtual:
`python -m venv enviroment`

## Ative o ambiente virtual
`enviroment\scripts\activate`

## Instale as dependências:
`pip install -r requirements.txt`

## Execute o script para importar os dados:
`python import_data.py`

## Construa a imagem Docker:
Execute o comando para construir a imagem Docker:
`docker build -t sprint_py .`

## Execute o contêiner Docker:
Após a construção da imagem, execute o contêiner:
`docker run -p 5000:5000 sprint_py`

## Acessando a aplicação
Abra o navegador web e navegue até http://localhost:5000/produtos.
