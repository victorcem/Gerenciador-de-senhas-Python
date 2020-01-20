# Importando o banco
import sqlite3
# Ajuste do menu
def titulo(msg):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)
# Senha primaria para teste
MASTER_PASSWORD = "123456789"

senha = input("Insira sua senha master: ")
if senha != MASTER_PASSWORD:
    titulo("Senha inválida! Encerrando ...")
    exit()
# criação do banco
conn = sqlite3.connect('password.db')

# coneção com o banco
cursor = conn.cursor()

# Tabela do Banco
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

# Menu principal
def menu():
    print("******************************")
    print("* i : inserir nova senha     *")
    print("* l : listar serviços salvos *")
    print("* r : recuperar uma senha    *")
    print("* s : sair                   *")
    print("******************************")
# Mostrar as senhas
def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        titulo('Serviço não encontrado (use l para verificar os serviços).')
    else:
        for user in cursor.fetchall():
            titulo(user)
# inserir senhas
def insert_passaword(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

# Mostrar todos os serviços
def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        titulo(service)

# Laço principal do menu
while True:
    menu()
    op = input("O que deseja fazer? ")
    if op not in ['l', 'i', 'r' ,'s']:
        titulo("Opção inváida!")
        continue
    
    if op == 'i':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuario? ')
        password = input('Qual a senha? ')
        insert_passaword(service, username, password)
    
    if op == 'l':
        show_services()

    if op == 'r':
        service = input('Qual serviço para qual quer a senha?  ')
        get_password(service)

    if op == 's':
        break

conn.close()