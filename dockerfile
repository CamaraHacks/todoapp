FROM python:3.11-slim

WORKDIR /app

# Copia os arquivos de dependências primeiro (para cache)
COPY src/pyproject.toml src/uv.lock .

# Instala UV e sincroniza dependências
RUN pip install uv
RUN uv sync --frozen

# Copia o resto do código
COPY src/ .

EXPOSE 8000

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
