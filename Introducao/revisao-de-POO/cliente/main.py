import socket

class BaixadorArquivo():

    def __init__(self, ip: str = 'localhost', porta: int = 4000):
        self.ip = ip
        self.porta = porta
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def realiza_conexao(self):
        self.cliente.connect( (self.ip, self.porta) )



    def baixa_arquivo(self, nome_arquivo: str, login: bool):


        if login:

            self.realiza_conexao()
            self.cliente.send(nome_arquivo.encode())

            try:
                with open (f'./arquivos/{nome_arquivo}', 'wb') as arquivo:

                    while True:

                        recebido = self.cliente.recv(1024)

                        if not recebido or recebido == b'Arquivo menor que o esperado' or recebido == b'Arquivo nao encontrado no servidor':
                            print(recebido.decode())
                            break
                        else:
                            arquivo.write(recebido)
                
                print('Arquivo baixado com sucesso do servidor')
            
            except Exception as erro:
                print('Falha ao baixar arquivo do servidor: ' + erro)




class Cliente(BaixadorArquivo):

    def __init__(self, nome: str = None, email: str = None, senha: str = None):

        super().__init__()
        self._nome = nome
        self._email = email
        self.__senha = senha



    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha



    def registrar(self):

        print('======= Registro =======')

        novo_email: str = str(input('Digite um novo e-mail: '))
        nova_senha: str = str(input('Digite uma nova senha: '))

        if self._email == None and self.senha == None:
            self._email = novo_email
            self.senha = nova_senha
            print('Cliente cadastrado com sucesso')
        else: 
            print('Cliente já registrado')
    


    def logar(self):

        print('=======  Login   =======')

        email: str = str(input('Digite um novo e-mail: '))
        senha: str = str(input('Digite uma nova senha: '))

        if email == self._email and senha == self.senha:
            print('Cliente logado com sucesso')
            return True
        else:
            print('Falha ao logar cliente')
            return False




    def __str__(self):
        return f'nome: {self._nome}, e-mail: {self._email}, senha: {self.senha}'

    

joaozin: Cliente = Cliente(nome='Aurora Fabiana Letícia Silveira')

joaozin.registrar()
joaozin.baixa_arquivo(nome_arquivo='meu_arquivo', login=joaozin.logar())


print(joaozin.__str__())