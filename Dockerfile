# Criação da imagem base
FROM python:3.9

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala todas as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte para o diretório de trabalho
COPY . .

# Execute a importação dos dados
RUN python import_data.py

# Exponha a porta em que a aplicação Flask será executada
EXPOSE 5000

# Define o comando de execução da API
CMD ["flask", "run", "--host=0.0.0.0"]