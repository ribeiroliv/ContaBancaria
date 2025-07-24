"""Pacote para gerenciamentode banco de dados"""
import sqlite3, os

cursor = None
conn = None

def conectar_banco():
    try:
        global cursor, conn
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()

        return True
    except Exception as e:
        print(f"Erro ao conectar banco de dados: {e}")

def criar_tabelas():
    try:
        conectar_banco()


        cursor.execute("""           
        CREATE TABLE IF NOT EXISTS Contas (
            numero integer PRIMARY KEY autoincrement,
            cliente_cpf integer NOT NULL,
            saldo real default 0 NOT NULL,
            limite real,
            tipo varchar(15) NOT NULL,
            ativo boolean default True,                                    
            FOREIGN KEY (cliente_cpf) REFERENCES Clientes(cpf)
        );
        """)

        cursor.execute("""  
        CREATE TABLE IF NOT EXISTS Historico (
            id integer PRIMARY KEY autoincrement,
            conta integer,
            tipooperacao varchar(100) NOT NULL,
            descricao varchar(250),
            valor real,
            contadestino integer,
            datahorario datetime,
            FOREIGN KEY (conta) REFERENCES Contas(numero)
            FOREIGN KEY (contadestino) REFERENCES Contas(numero)
        );
        """)
        conn.commit()
        print("\nTabelas criadas com sucesso!\n")

    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
        conn.rollback()

    conn.close()

def listar_tabelas():
    try:
        conectar_banco()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tabelas = cursor.fetchall()

        print("Tabelas de banco de dados: ")
       
        if tabelas:
            for index, tabela in enumerate(tabelas):
                print(f"    {index+1}. {tabela[0]}")
        else:
            print("Nenhum registro encontrado.")
        print()

    except Exception as e:
        print(f"Erro ao realizar consulta: {e}")
    conn.close()

def apagar():
    cursor.execute("DROP TABLE IF EXISTS Clientes")

def cadastrar_cliente():
    try:
        conectar_banco()
        # Verifica/Cria a tabela se não existir
        cursor.execute("""
                    
        CREATE TABLE IF NOT EXISTS Clientes (
            cpf varchar(11) PRIMARY KEY,
            nome text NOT NULL,
            sobrenome text NOT NULL,
            datanasc text NOT NULL,
            telefone varchar(13),
            email varchar(100),
            endereco text,
            cidade text,
            uf varchar(2),
            senha varchar(255),
            ativo boolean default True                                    
        );

            
        """)
        conn.commit()
        print("\nTabelas criadas com sucesso!\n")

    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
        conn.rollback()

    conn.close()

def criar_conta():
    try:
        # Primeiro drope a tabela existente (CUIDADO: isso apagará todos os dados)
        cursor.execute("DROP TABLE IF EXISTS Contas")

        # Crie a tabela com a nova estrutura
        cursor.execute("""           
        CREATE TABLE IF NOT EXISTS Contas (
            numero integer PRIMARY KEY autoincrement,
            cliente_cpf varchar(11) NOT NULL,
            saldo real default 0 NOT NULL,
            limite real,
            tipo varchar(15) NOT NULL,
            agencia varchar(10) NOT NULL,
            ativo boolean default True,                                    
            FOREIGN KEY (cliente_cpf) REFERENCES Clientes(cpf)
        );
        """)
        conn.commit()
        print("\nTabelas criadas com sucesso!\n")

    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
        conn.rollback()

    conn.close()

if __name__ == "__main__":
    conectar_banco()
    while True:
        print()
        print("################################--------################################")
        print("Seja bem vindo ao menu de gerenciamento do banco de dados no seu sistema: ")

        try:
            print()
            op = int(input("""\nSelecione a opção do menu conforme:
            1 - Criar banco de dados
            2 - Criar tabelas
            3 - Listar tabelas do banco de dados
            0 - Sair
            """))

           

            if op == 1:
                conectar_banco()
            elif op == 2:
                criar_tabelas()
            elif op == 3:
                listar_tabelas()
            elif op == 4:
                cadastrar_cliente()
            elif op == 5:
                criar_conta()
            elif op == 0:
                break
            else:
                continue
            
        except ValueError:
            print("Opção inválida")
            continue

conectar_banco() 