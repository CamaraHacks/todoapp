# ✅ TodoApp - Gerenciador de Tarefas

Um sistema simples e eficiente de gerenciamento de tarefas desenvolvido com **Django 5.2** e **Python 3.13**, utilizando o moderno gerenciador de pacotes **uv**.

## 🚀 Funcionalidades

- **Autenticação de Usuário**: Cada usuário possui sua própria lista de tarefas (isolamento por usuário).
- **CRUD de Tarefas**: Criar, visualizar, editar e excluir tarefas.
- **Priorização**: Definição de níveis de prioridade com indicadores visuais:
  - 🟢 Baixa
  - 🟡 Média
  - 🔴 Alta
  - ⚡ Urgente
  
- **Controle de Status**: Marcar tarefas como concluídas (com registro automático da data de conclusão).
- **Interface Responsiva**: Templates HTML limpos e organizados.
- **Infraestrutura Pronta**: Suporte total a Docker e PostgreSQL.

## 🛠️ Stack Tecnológica

- **Linguagem**: Python 3.13
- **Framework Web**: Django 5.2
- **Banco de Dados**: PostgreSQL 16
- **Gerenciador de Pacotes**: [uv](https://github.com/astral-sh/uv)
- **Servidor de Aplicação**: Gunicorn
- **Arquivos Estáticos**: WhiteNoise
- **Containerização**: Docker & Docker Compose
- **Testes**: Pytest

## 🏗️ Modelagem de Dados (Decisões de Projeto)

O modelo principal é o `Task`, projetado para ser flexível e informativo:

- **`user`**: Relacionamento `ForeignKey` com o modelo `User` padrão do Django. Garante que cada usuário acesse apenas seus dados.
- **`priority`**: Campo `CharField` com `choices`. A escolha de emojis diretamente no banco/modelo visa facilitar a renderização visual imediata no front-end.
- **`completed_date`**: Diferente de apenas um booleano, este campo permite futuras análises de produtividade (ex: quanto tempo levou para terminar).
- **`Meta Ordering`**: Ordenação padrão por status de conclusão e data de criação para manter as tarefas pendentes sempre no topo.

## 📁 Estrutura do Projeto

```text
.
├── tarefas/          # Configurações globais do projeto Django
├── todo/             # Aplicação principal (Lógica de tarefas)
├── infra/            # Arquivos de infraestrutura (Dockerfile)
├── staticfiles/      # Arquivos estáticos coletados
├── docker-compose.yml# Orquestração de serviços (Web + DB)
├── pyproject.toml    # Definição de dependências (uv)
└── manage.py         # Utilitário de gerenciamento do Django
```

## ⚙️ Como Executar

### Utilizando Docker (Recomendado)

1. Certifique-se de ter o Docker instalado.
2. Clone o repositório.
3. Execute:
   ```bash
   docker-compose up --build
   ```
4. O servidor estará disponível em `http://localhost:8000`.

### Desenvolvimento Local (com `uv`)

1. Instale o `uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Sincronize o ambiente:
   ```bash
   uv sync
   ```
3. Configure o banco de dados no arquivo `.env`.
4. Execute as migrações:
   ```bash
   uv run python manage.py migrate
   ```
5. Inicie o servidor:
   ```bash
   uv run python manage.py runserver
   ```

## 🧪 Testes

O projeto utiliza `pytest`. Para rodar a suíte de testes:

```bash
uv run pytest
```

---
*Desenvolvido para ser simples, extensível e moderno.*
