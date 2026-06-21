# PhoneMassShoterPy

Sistema desenvolvido em Python para automatizar o envio de mensagens em massa durante processos de recrutamento e seleção, utilizando a API do WhatsApp da Z-API e o Supabase como banco de dados.

O projeto foi criado para organizar o fluxo de contatos, evitar envios duplicados e facilitar o acompanhamento do status de cada candidato durante uma seleção de estágio.

## Como funciona

O sistema segue uma arquitetura em camadas:

```
Controllers → Services → Repositories → Database
```

### Fluxo de execução

1. Os números de telefone são cadastrados no banco de dados.
2. O sistema consulta os contatos pendentes.
3. As mensagens são enviadas através da Z-API.
4. O resultado da operação é registrado no banco.
5. Logs são gerados para facilitar auditoria e depuração.

Dessa forma é possível controlar quais contatos já receberam mensagens, quais falharam e quais ainda estão aguardando processamento.

## Tecnologias Utilizadas

* Python 3.10+
* SQLAlchemy
* PostgreSQL (Supabase)
* Z-API (WhatsApp API)
* Requests
* Python Dotenv

## Estrutura do Projeto

```
PhoneMassShoterPy/
│
├── main.py
├── requirements.txt
├── logs/
│
└── src/
    ├── controllers/
    ├── database/
    ├── models/
    ├── repositories/
    ├── services/
    └── views/
```

### Camadas

#### Controllers

Responsáveis por receber comandos da aplicação e iniciar os fluxos de execução.

#### Services

Contêm as regras de negócio, processamento de dados e integração com APIs externas.

#### Repositories

Realizam o acesso ao banco de dados através dos modelos definidos na aplicação.

#### Database

Gerencia a conexão com o PostgreSQL/Supabase.

#### Models

Representam as entidades e estruturas utilizadas pelo sistema.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/HandreyGama/PhoneMassShoterPy.git
cd PhoneMassShoterPy
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Windows:

```bash
.\.venv\Scripts\activate
```

Linux:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
user=SEU_USUARIO_POSTGRES
password=SUA_SENHA_POSTGRES
host=SEU_HOST_SUPABASE
port=5432
dbname=postgres

zapi_instance=SUA_INSTANCIA
zapi_instance_token=SEU_TOKEN
```

## Configurando o Supabase

1. Crie uma conta no Supabase.
2. Crie um novo projeto.
3. Acesse:

```
Project Settings → Database
```

4. Copie as informações de conexão:

   * Host
   * Database Name
   * User
   * Password
   * Port

5. Preencha os valores no arquivo `.env`.

## Configurando a Z-API

1. Crie uma conta na Z-API.

2. Crie uma nova instância.

3. Conecte o WhatsApp via QR Code.

4. Copie:

   * Instance ID
   * Instance Token

5. Adicione essas informações ao arquivo `.env`.

## Executando

Após configurar o ambiente:

```bash
python main.py
```

Ou:

```bash
python main.py --type script
```

## Logs

Os logs da aplicação são armazenados em:

```text
logs/logs.txt
```

Eles registram eventos importantes como:

* Envios realizados
* Falhas de comunicação
* Erros de API
* Problemas de banco de dados

## Objetivo do Projeto

Além de resolver um problema real de automação para processos seletivos, este projeto também serve como estudo de:

* Arquitetura em camadas
* Integração com APIs REST
* SQLAlchemy
* PostgreSQL
* Padrão Repository
* Organização de projetos Python
* Boas práticas de desenvolvimento backend

## Licença

Este projeto está disponível para fins educacionais e de estudo.
