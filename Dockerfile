# 1. Imagem base: usamos uma versão leve (slim) do Python 3.12
FROM python:3.12-slim

# 2. Variáveis de ambiente para o Python não criar arquivos inúteis (.pyc) 
# e para os logs aparecerem em tempo real no terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Define onde o código vai morar dentro do container
WORKDIR /app

# 4. Instala dependências do sistema necessárias (opcional, mas bom ter)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia primeiro apenas o arquivo de requisitos
# Fazemos isso para que o Docker use o "cache" e não precise reinstalar 
# tudo toda vez que você mudar uma linha de código.
COPY requirements.txt .

# 6. Instala as bibliotecas do Python
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copia todo o resto do seu projeto para dentro do container
COPY . .

# 8. Expõe a porta que o Django usa por padrão
EXPOSE 8000

# 9. Comando para rodar a aplicação
# Para o trabalho, o "runserver" resolve, mas o 0.0.0.0 é obrigatório para o Docker
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
