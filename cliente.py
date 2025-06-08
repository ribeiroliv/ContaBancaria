import bd2

class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
    
    @staticmethod
    def verificar_nome(nome):
        try:
            if len(nome) > 3 and ' ' in nome:
                return True
            else:
                print("Digite um nome válido")
                return False
        except TypeError:
            print(f"Aconteceu o erro: Você passou um número ao invés de um nome")
            
            return False

    @staticmethod
    def verificar_cpf(cpf):
        if len(cpf) == 11:
            return True
        else:
            print("Insira o CPF correto")
            return False
        
    @staticmethod
    def cadastrar( ): #para os dados do banco
        try:
            nome = input('insira seu nome: ')
            sobrenome = input('insira seu sobrenome: ')
            cpf = input('insira seu cpf: ')
            datanasc = input('insira sua data de nascimento: ')
            telefone = input('insira seu telefone: ')
            email = input('insira seu email: ')
            endereco =  input('digite seu endereço: ')
            cidade = input('insira sua cidade: ')
            uf = input('insira sua uf: ')

            bd2.cursor.execute("""
                INSERT INTO Clientes(nome, sobrenome, cpf, datanasc, telefone, email, endereco, cidade, uf)
                VALUES(?,?,?,?,?,?,?,?,?)
            """, (nome, sobrenome, cpf, datanasc, telefone, email, endereco, cidade, uf))
            bd2.conn.commit()

            print('Cliente cadastrado!')
        except Exception as e:
            print(f'erro ao cadastrar em {e}')
