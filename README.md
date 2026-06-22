# Sistema de Biblioteca

Projeto em Python para gerenciar livros, usuarios e emprestimos de uma biblioteca. O sistema pode ser usado pelo terminal ou por uma tela visual simples feita com Flask.

## Tecnologias usadas

- Python
- Flask
- SQLite
- HTML
- CSS
- Programacao modular

## Como usar a tela visual

1. Instale as dependencias:

```bash
pip install -r requirements.txt
```

2. Inicie o sistema web:

```bash
python app.py
```

3. Abra no navegador:

```text
http://127.0.0.1:5000
```

Na tela inicial voce encontra botoes para acessar:

- Livros
- Usuarios
- Emprestimos

## Como usar pelo terminal

Execute:

```bash
python main.py
```

O menu do terminal permite navegar pelas funcoes de livros, usuarios e emprestimos usando numeros.

## Funcionalidades atuais

- Cadastro de livros
- Listagem e busca de livros
- Edicao de livros
- Exclusao de livros disponiveis
- Cadastro de usuarios
- Listagem e busca de usuarios
- Edicao de usuarios
- Exclusao de usuarios sem emprestimos ativos
- Registro de emprestimos
- Registro de devolucoes
- Controle de livros disponiveis e emprestados

## Banco de dados

O projeto usa SQLite e salva os dados em:

```text
Banco/biblioteca.db
```

As tabelas principais sao:

- `livros`
- `usuarios`
- `emprestimos`

As tabelas sao criadas automaticamente quando o sistema inicia.

## Estrutura do projeto

```text
BibiotlecaPythonV1/
├── app.py
├── main.py
├── requirements.txt
├── Banco/
├── Cadastros/
├── Edicoes/
├── Emprestimos/
├── Exclusoes/
├── Menus/
├── Pesquisas/
├── Utils/
├── Validacoes/
├── templates/
└── static/
```

## Futuras atualizacoes

- Tela de login para administrador
- Historico completo de emprestimos e devolucoes
- Controle de atraso na devolucao
- Relatorios de livros mais emprestados
- Melhor mascara para CPF e datas
- Confirmacao visual antes de excluir registros
- Pagina de detalhes para cada livro e usuario
- Exportacao de dados para planilha
