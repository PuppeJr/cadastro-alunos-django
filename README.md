# 📚 Cadastro de Alunos – Django CRUD

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0%2B-green)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-blueviolet)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Projeto desenvolvido na disciplina de Programação III** – Curso Tecnologia em Análise e Desenvolvimento de Sistemas (3º semestre) – IFRS.

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação e Execução](#instalação-e-execução)
  - [Clonando o repositório](#clonando-o-repositório)
  - [Configurando o ambiente virtual](#configurando-o-ambiente-virtual)
  - [Instalando dependências](#instalando-dependências)
  - [Aplicando migrações](#aplicando-migrações)
  - [Criando um superusuário](#criando-um-superusuário)
  - [Executando o servidor](#executando-o-servidor)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Como Usar](#como-usar)
- [Capturas de Tela](#capturas-de-tela)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Autor](#autor)
- [Contexto Acadêmico](#contexto-acadêmico)

---

## Sobre o Projeto

Este é um sistema web simples e funcional para **gerenciamento de alunos**, desenvolvido com o framework Django. Ele implementa todas as operações de um **CRUD** (Create, Read, Update, Delete) e foi construído para consolidar os fundamentos abordados nas aulas de Programação III, tais como:

- Criação e configuração de projetos e aplicações Django.
- Definição de modelos (Models) e migrações.
- Views baseadas em funções (FBV).
- Roteamento de URLs (global e por aplicação).
- Templates com herança (base.html e extensões).
- Passagem de contexto do backend para o frontend.
- Uso de ModelForms para validação e renderização de formulários.

O sistema é auto‑suficiente, utiliza o banco de dados SQLite (embutido) e pode ser executado localmente com poucos comandos.

---

## Funcionalidades

| Operação | Descrição |
|---|---|
| **📋 Listar Alunos** | Exibe todos os alunos cadastrados em uma tabela ordenada por nome. |
| **➕ Cadastrar Aluno** | Formulário para inserir nome, e-mail, telefone (opcional) e data de nascimento. |
| **✏️ Editar Aluno** | Permite atualizar os dados de um aluno existente. |
| **🗑️ Excluir Aluno** | Página de confirmação antes da exclusão definitiva. |
| **🔐 Painel Admin** | Interface administrativa do Django para gerenciar alunos com mais recursos. |

---

## Tecnologias Utilizadas

- **Python 3.8+** – Linguagem de programação.
- **Django 4.0+** – Framework web de alto nível.
- **SQLite3** – Banco de dados relacional (embutido).
- **Bootstrap 5.3** – Framework CSS para estilização responsiva.
- **HTML5 / CSS3** – Estrutura e estilização das páginas.
- **Git & GitHub** – Controle de versão e hospedagem do código.

---

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Python 3.8 ou superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/) (opcional, mas recomendado)
- [VS Code](https://code.visualstudio.com/) (recomendado) ou qualquer editor de texto.

---

## Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente.

### Clonando o repositório

```bash
git clone https://github.com/PuppeJr/cadastro-alunos-django.git
cd cadastro-alunos-django
```

### Configurando o ambiente virtual

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Instalando dependências

```bash
pip install -r requirements.txt
```

Caso não tenha o arquivo `requirements.txt`, instale o Django manualmente: `pip install django`

### Aplicando migrações

```bash
python manage.py migrate
```

### Criando um superusuário

```bash
python manage.py createsuperuser
```

### Executando o servidor

```bash
python manage.py runserver
```

Acesse o projeto no navegador através do endereço: `http://127.0.0.1:8000/`

---

## Estrutura de Diretórios

```text
cadastro-alunos-django/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── alunos/
    ├── migrations/
    ├── templates/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

---

## Como Usar

1. Após iniciar o servidor, acesse a página inicial para ver a lista de alunos.
2. Clique em **"Cadastrar Aluno"** para adicionar um novo registro.
3. Na listagem, você pode clicar em **"Editar"** ou **"Excluir"** nas ações de cada aluno.
4. Para acessar o painel administrativo, vá para `http://127.0.0.1:8000/admin/` e faça login com o superusuário criado.

---

## Capturas de Tela

Adicione aqui as imagens do seu projeto, por exemplo:

<!-- ![Listagem de Alunos](docs/listagem.png) -->
<!-- ![Formulário de Cadastro](docs/cadastro.png) -->

---

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

1. Faça um *fork* do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um *Pull Request*.

---

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Autor

Desenvolvido por **PuppeJr**.

---

## Contexto Acadêmico

Este projeto foi desenvolvido como atividade avaliativa da disciplina de **Programação III**, do curso de Tecnologia em Análise e Desenvolvimento de Sistemas (3º semestre) do **IFRS** (Instituto Federal do Rio Grande do Sul). O objetivo principal foi aplicar os conceitos de desenvolvimento web com Python e Django, focando na criação de um CRUD completo e na integração entre backend e frontend.
