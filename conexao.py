import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega as informações do arquivo .env
load_dotenv()

# Obtém a string de conexão
MONGO_URI = os.getenv("MONGO_URI")

# Verifica se a conexão foi configurada
if not MONGO_URI:
    raise ValueError("MONGO_URI não encontrada no arquivo .env")

# Cria a conexão com o MongoDB (espera até 20 segundos)
cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=20000)

# Testa a conexão (ping) e mantém o cliente aberto
cliente.admin.command("ping")

# Seleciona o banco de dados
banco = cliente["agenda_contatos"]

print("================================")
print(" CONEXÃO REALIZADA COM SUCESSO!")
print(f" Banco: {banco.name}")
print("================================")