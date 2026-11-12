# 📇 Agenda de Contatos — Python + MongoDB

Projeto 04 da trilha "MongoDB + Python — 10 Projetos Práticos" (disciplina de Banco de Dados, 4º bimestre).

**Autor(a):** Luiz Otávio Ferreira Jardim/ Nicolas Landin Cassal dos Santos/ Thiago Teodoro Costa · **Turma:** 2°i

## Objetivo

Criar uma agenda de contatos em linha de comando que permita adicionar, buscar, atualizar e remover contatos, armazenando os dados no MongoDB Atlas (nuvem).

## Ambiente

- Python 3.14
- MongoDB Atlas (cluster na nuvem)
- Bibliotecas: `pymongo`, `python-dotenv`
- Editor: Visual Studio Code

## Estrutura do projeto

```
AgendaDeContatos/
├── conexao.py    # conexão com o MongoDB Atlas
├── main.py       # menu e operações da agenda
├── .env          # string de conexão (NÃO é publicado)
└── .gitignore
```

## Como executar

1. Instale as dependências:
   ```
   py -m pip install pymongo python-dotenv
   ```
2. Crie um arquivo `.env` na pasta do projeto com a sua string de conexão:
   ```
   MONGO_URI=sua_string_de_conexao_do_atlas
   ```
3. Execute o programa:
   ```
   py main.py
   ```

## Modelo de dados

Banco: `agenda_contatos` · Coleção: `contatos`

Exemplo de documento:

```json
{
  "nome": "Ana Silva",
  "email": "ana@email.com",
  "telefone": "12988887777"
}
```

Índice: `email` com **índice único**, o que impede dois contatos com o mesmo e-mail.

## Funcionalidades

| Opção | Ação | Operação MongoDB |
|---|---|---|
| 1 | Adicionar contato | `insert_one` |
| 2 | Buscar por parte do nome (sem diferenciar maiúsculas) | `find` com `$regex` |
| 3 | Atualizar telefone pelo e-mail | `update_one` com `$set` |
| 4 | Remover contato pelo e-mail | `delete_one` |

## Desafio extra implementado

**Validação do formato do e-mail** com expressão regular: e-mails fora do padrão `nome@dominio.com` (por exemplo `abc` ou `ana@`) são recusados antes de salvar.

## Testes realizados

| Teste | Entrada | Resultado esperado | Resultado |
|---|---|---|---|
| Campo vazio | Nome em branco | "O nome é obrigatório." | ✅ |
| Cadastro | Ana Silva, ana@email.com | "Contato salvo!" | ✅ |
| E-mail duplicado | ana@email.com de novo | "E-mail já utilizado." | ✅ |
| Busca sem diferenciar maiúsculas | `ana` | Retorna Ana Silva | ✅ |
| Atualização | Novo telefone da Ana | "Atualizado!" | ✅ |
| Remoção | E-mail do Bruno | "Excluído!" | ✅ |
| E-mail inválido | `abc` e `ana@` | "E-mail inválido." | ✅ |

## Problemas encontrados e soluções

- **Comando `python` não executava no PowerShell:** foi usado o launcher `py`.
- **Timeout na conexão com o Atlas:** o tempo de espera foi aumentado de 5 para 20 segundos e o DNS foi verificado com `Resolve-DnsName`.
- **Erro "Cannot use MongoClient after close":** o `cliente.close()` no bloco `finally` do `conexao.py` fechava a conexão antes do uso; ele foi removido.

## Segurança

O arquivo `.env` contém a senha do banco e está listado no `.gitignore`, portanto **não é enviado ao GitHub**.