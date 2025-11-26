import psycopg2

con = psycopg2.connect(
    host="pg-28d1957e-omena-e549.d.aivencloud.com",
    port=20799,
    database="futliga",
    user="avnadmin",
    password="senhaqueestanodoc",
    sslmode="require"
)

cur = con.cursor()

def inserir():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    pos = input("Posição: ")
    data = input("Data nascimento (YYYY-MM-DD): ")
    nac = input("Nacionalidade: ")
    time = input("CNPJ do time: ")
    adm = input("CPF do adm: ")
    
    cur.execute("""
        INSERT INTO Jogador (cpf, nome, posicao, datanascimento, nacionalidade, timecnpj, admcpf)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (cpf, nome, pos, data, nac, time, adm))
    con.commit()
    print("Jogador inserido!\n")

def listar():
    cur.execute("SELECT cpf, nome, posicao, nacionalidade FROM Jogador")
    for row in cur.fetchall():
        print(row)
    print()

def atualizar():
    cpf = input("CPF do jogador que deseja atualizar: ")
    novo_nome = input("Novo nome: ")

    cur.execute("""
        UPDATE Jogador SET nome = %s WHERE cpf = %s
    """, (novo_nome, cpf))
    con.commit()
    print("Jogador atualizado!\n")

def excluir():
    cpf = input("CPF do jogador a excluir: ")
    cur.execute("DELETE FROM Jogador WHERE cpf = %s", (cpf,))
    con.commit()
    print("Jogador excluído!\n")

while True:
    print("""
1 - Inserir jogador
2 - Listar jogadores
3 - Atualizar jogador
4 - Excluir jogador
0 - Sair
""")
    op = input("Opção: ")

    if op == "1": inserir()
    elif op == "2": listar()
    elif op == "3": atualizar()
    elif op == "4": excluir()
    elif op == "0":
        break
    else:
        print("Opção inválida!")
