import socket
import os

class BaixadorArquivo():

    def __init__(self, ip: str = 'localhost', porta: int = 4000):
        
        super().__init__()
        self.ip = ip
        self.porta = porta
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def realiza_conexao(self):
        self.cliente.connect( (self.ip, self.porta) )



    def upload_arquivo(self, nome_arquivo: str, login: bool):


        if login:

            if os.path.getsize(f'arquivos/{nome_arquivo}')*8 >= 250:

                self.realiza_conexao()

                self.cliente.send(nome_arquivo.encode())

                arquivo_lido = b''

                try:
                    with open(f'./arquivos/{nome_arquivo}', 'r') as arquivo:
                        for linha in arquivo.readlines():
                            arquivo_lido += linha.encode()
                    print(f'{nome_arquivo} lido com sucesso')
                except:
                    print(f'Falha ao ler {nome_arquivo}')


                try:
                    self.cliente.send(arquivo_lido)
                    print(f'{nome_arquivo} enviado com sucesso')
                except:
                    print(f'Falha ao enviar {nome_arquivo}')

            else:
                print('Falha ao enviar arquivo: Arquivo menor que 250 Mb')

        else:
            print('Falha ao iniciar upload: login inválido')





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

    

aurora: Cliente = Cliente(nome='Aurora Fabiana Letícia Silveira')



aurora.registrar()

aurora.upload_arquivo(nome_arquivo='meu_arquivo.txt', login=aurora.logar())

print(aurora.__str__())