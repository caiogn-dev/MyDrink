# MyDrink - Sistema de Gerenciamento de Bebidas

## Descrição
MyDrink é um sistema web desenvolvido em Django para gerenciamento de bebidas, com funcionalidades de cadastro, controle de estoque, vendas e relatórios.

## Requisitos
- Python 3.11+
- PostgreSQL 14+
- Redis 6+
- Node.js 18+ (para assets)
- Virtualenv (recomendado)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/caiogn-dev/MyDrink.git
cd mydrink
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Configure o banco de dados:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## Configuração do Ambiente

### Variáveis de Ambiente
Copie o arquivo `.env.example` para `.env` e configure as seguintes variáveis:

- `DEBUG`: Modo de debug (True/False)
- `SECRET_KEY`: Chave secreta do Django
- `DATABASE_URL`: URL de conexão com o PostgreSQL
- `REDIS_URL`: URL de conexão com o Redis
- `EMAIL_*`: Configurações de email
- `AWS_*`: Configurações do AWS S3 (se necessário)

### Banco de Dados
O projeto utiliza PostgreSQL como banco de dados principal. Certifique-se de ter o PostgreSQL instalado e configurado antes de iniciar o projeto.

### Redis
O Redis é utilizado para cache e filas de tarefas. Instale e configure o Redis antes de iniciar o projeto.

## Estrutura do Projeto

```
mydrink/
├── apps/                    # Aplicações Django
│   ├── core/               # Funcionalidades principais
│   ├── inventory/          # Gerenciamento de estoque
│   ├── sales/              # Gerenciamento de vendas
│   └── reports/            # Relatórios
├── config/                 # Configurações do projeto
├── static/                 # Arquivos estáticos
├── templates/              # Templates HTML
├── tests/                  # Testes
└── manage.py              # Script de gerenciamento
```

## Desenvolvimento

### Convenções de Código
- Siga o PEP 8 para Python
- Utilize Black para formatação
- Utilize Flake8 para linting
- Utilize MyPy para verificação de tipos

### Testes
```bash
pytest
```

### Deploy
O projeto está configurado para deploy em ambientes de produção. Consulte a documentação de deploy para mais informações.

## Segurança
- Todas as senhas são armazenadas com hash
- Proteção contra CSRF
- Rate limiting configurado
- Headers de segurança configurados
- Logs de auditoria implementados

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes. 
