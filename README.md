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
  - [Criando um superusuário (opcional)](#criando-um-superusuário-opcional)
  - [Executando o servidor](#executando-o-servidor)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Como Usar](#como-usar)
- [Capturas de Tela](#capturas-de-tela)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Autor](#autor)
- [Contexto Acadêmico](#contexto-acadêmico)

---

## 📖 Sobre o Projeto

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

## ⚙️ Funcionalidades

| Operação | Descrição |
|----------|-----------|
| **📋 Listar Alunos** | Exibe todos os alunos cadastrados em uma tabela ordenada por nome. |
| **➕ Cadastrar Aluno** | Formulário para inserir nome, e-mail, telefone (opcional) e data de nascimento. |
| **✏️ Editar Aluno** | Permite atualizar os dados de um aluno existente. |
| **🗑️ Excluir Aluno** | Página de confirmação antes da exclusão definitiva. |
| **🔐 Painel Admin** | Interface administrativa do Django para gerenciar alunos com mais recursos. |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** – Linguagem de programação.
- **Django 4.0+** – Framework web de alto nível.
- **SQLite3** – Banco de dados relacional (embutido).
- **Bootstrap 5.3** – Framework CSS para estilização responsiva.
- **HTML5 / CSS3** – Estrutura e estilização das páginas.
- **Git & GitHub** – Controle de versão e hospedagem do código.

---

## 🧩 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Python 3.8 ou superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/) (opcional, mas recomendado)
- [VS Code](https://code.visualstudio.com/) (recomendado) ou qualquer editor de texto.

---

## 🚀 Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente.

### Clonando o repositório

```bash
git clone https://github.com/PuppeJr/cadastro-alunos-django.git
cd cadastro-alunos-django
