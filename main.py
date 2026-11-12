"""Projeto 04: Agenda de Contatos com MongoDB (filtro por nome e indice unico)."""
import re
from pymongo.errors import DuplicateKeyError
from conexao import banco

contatos = banco['contatos']
contatos.create_index('email', unique=True)  # impede e-mails repetidos

# Desafio extra: validação do formato do e-mail (ex.: nome@dominio.com)
PADRAO_EMAIL = re.compile(r'^[\w.+-]+@[\w-]+(\.[\w-]+)+$')


def email_valido(email):
    return bool(PADRAO_EMAIL.match(email))


while True:
    print('\n[1] Adicionar [2] Buscar [3] Atualizar [4] Remover [0] Sair')
    op = input('Opção: ').strip()

    if op == '1':
        nome = input('Nome: ').strip()
        if not nome:
            print('O nome é obrigatório.')
            continue
        email = input('E-mail: ').strip().lower()
        if not email:
            print('O e-mail é obrigatório.')
            continue
        if not email_valido(email):
            print('E-mail inválido. Use o formato nome@dominio.com')
            continue
        telefone = input('Telefone: ').strip()
        if not telefone:
            print('O telefone é obrigatório.')
            continue
        try:
            contatos.insert_one({'nome': nome, 'email': email, 'telefone': telefone})
            print('Contato salvo!')
        except DuplicateKeyError:
            print('E-mail já utilizado.')

    elif op == '2':
        trecho = input('Parte do nome: ').strip()
        if not trecho:
            print('Informe um termo.')
            continue
        busca = {'nome': {'$regex': re.escape(trecho), '$options': 'i'}}
        encontrou = False
        for item in contatos.find(busca, {'_id': 0}).sort('nome'):
            print(item)
            encontrou = True
        if not encontrou:
            print('Nenhum contato encontrado.')

    elif op == '3':
        email = input('E-mail do contato: ').strip().lower()
        telefone = input('Novo telefone: ').strip()
        if telefone:
            r = contatos.update_one({'email': email}, {'$set': {'telefone': telefone}})
            print('Atualizado!' if r.matched_count else 'Contato não encontrado.')

    elif op == '4':
        email = input('E-mail: ').strip().lower()
        r = contatos.delete_one({'email': email})
        print('Excluído!' if r.deleted_count else 'Contato não encontrado.')

    elif op == '0':
        break

    else:
        print('Opção inválida.')