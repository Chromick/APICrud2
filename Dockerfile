# Usar a imagem base do Python
FROM python:3.9

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar todo o código
COPY . .

# Expor a porta da aplicação
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]