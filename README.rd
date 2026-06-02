Sistema de Biblioteca em Python

Projeto desenvolvido para fins de estudo e portfólio, com foco na aplicação de conceitos fundamentais de desenvolvimento de software utilizando Python e SQLite.

O sistema funciona totalmente via terminal (CLI) e atualmente possui um CRUD completo para gerenciamento de livros, além de uma estrutura modular preparada para futuras expansões.

Tecnologias Utilizadas:

- Python
- SQLite3
- Programação Modular
- SQL

Funcionalidades Atuais:

- Cadastro de Livros

Permite registrar livros contendo:

- Nome do livro
- Descrição
- Estado do livro
- Entregue por
- Status do livro

Consulta de Livros:

Permite:

- Buscar por ID
- Buscar por nome utilizando LIKE
- Listar todos os livros
- Listar livros disponíveis
- Listar livros emprestados

Edição de Livros:

Sistema de edição interativo que:

- Atualiza informações em tempo real
- Exibe ao usuário quais alterações foram realizadas
- Permite alterar campos individualmente

Exclusão de Livros:

- Confirmação antes da exclusão
- Remoção segura dos registros

Boas Práticas Aplicadas:

- Separação entre interface e banco de dados
- Modularização das funcionalidades
- Consultas SQL centralizadas
- Validação de entradas do usuário
- Tratamento de exceções com try/except
- Persistência de dados com SQLite
- Inicialização automática do banco de dados
- Estrutura preparada para crescimento do projeto

Estrutura do Projeto:

Biblioteca/
│
├── main.py
├── menu.py
├── biblioteca.db
│
├── Importantes/
│   ├── db_config.py
│   ├── limpar_chat.py
│
├── menu_editar/
│   ├── editar_nome_livro.py
│   ├── editar_descricao_livro.py
│   ├── editar_condicao_livro.py
│
├── menu_procurar/
│   ├── procurar_nome.py
│   ├── procurar_id.py
│   ├── procurar_disponiveis.py
│   ├── procurar_emprestados.py
│
└── demais módulos...

Banco de Dados:

Tabela atual:

sql livros

Campos:

sql
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome_livro TEXT,
descricao_livro TEXT,
estado_livro TEXT,
entregue_por TEXT,
status INTEGER

Funcionalidades Futuras:

Cadastro de Usuários:

- Nome
- CPF
- Idade
- Data de cadastro
- Status de empréstimo

Sistema de Empréstimos:

- Registro de empréstimos
- Controle de devoluções
- Data e hora do empréstimo
- Data prevista de devolução
- Controle de atrasos
- Histórico de movimentações

Configurações Administrativas:

Limite configurável de livros por usuário
Regras personalizadas para diferentes cenários de uso

Objetivo do Projeto:

Este projeto foi desenvolvido como parte do meu processo de aprendizado em Python, banco de dados e organização de software. O objetivo é demonstrar evolução técnica, aplicação de boas práticas e construção de soluções reais utilizando tecnologias amplamente utilizadas no mercado.
