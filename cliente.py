import bd2
from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
    
    #Funções de Validação:
    @staticmethod
    def verificar_nome(nome):
        try:
            nome = nome.strip()  # Remove espaços no início e fim
            if len(nome) < 3:
                print('Nome deve ter pelo menos 3 caracteres')
                return False
            
            if not all(c.isalpha() or c.isspace() for c in nome):
                print('Nome deve conter apenas letras e espaços')
                return False
            
            return True
        
        except AttributeError:  # Captura caso não seja string
            print('Você passou um valor inválido (não é texto)')

            return False

    @staticmethod
    def verificar_cpf(cpf):
        if len(cpf) == 11:
            return True
        else:
            print('Insira o CPF correto')
            return False
        
        
    @staticmethod
    def cadastrar( ): #para os dados do banco
        try:
            cpf = input('insira seu cpf: ')
            nome = input('insira seu nome: ')
            sobrenome = input('insira seu sobrenome: ')
            datanasc = input('insira sua data de nascimento: ')
            telefone = input('insira seu telefone: ')
            email = input('insira seu email: ')
            endereco =  input('digite seu endereço: ')
            cidade = input('insira sua cidade: ')
            uf = input('insira sua uf: ')

            # -->Validaçoes<--
            if not Cliente.verificar_nome(nome):
                return False
            if not Cliente.verificar_nome(sobrenome):
                return False
            if not Cliente.verificar_cpf(cpf):
                return False



            bd2.cursor.execute("""
                INSERT INTO Clientes(cpf, nome, sobrenome, datanasc, telefone, email, endereco, cidade, uf)
                VALUES(?,?,?,?,?,?,?,?,?)
            """, (cpf, nome, sobrenome, datanasc, telefone, email, endereco, cidade, uf))
            bd2.conn.commit()

            print('Cliente cadastrado com sucesso!')
            return True
        except ValueError as ve:
            print(f'\nErro de validação: {ve}')
            return False
        except Exception as e:
            print(f'erro ao cadastrar em {e}')
            return False
            
