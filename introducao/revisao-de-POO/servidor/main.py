import socket
import os

class Servidor() :

    def __init__(self, ip:str = 'localhost', porta:int = 3000):

        self.ip = ip
        self.porta = porta
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        


    def escutar(self, quantidade_clientes:int = 1):
        try:
            self.servidor.bind((self.ip, self.porta))
            self.servidor.listen(quantidade_clientes)
        except:
            print('Falha ao ouvir clientes')



    def aceitar_conexao(self):
        try:
            return self.servidor.accept()
        except:
            print('Falha ao aceitar conexão')
            return (None, None)



    def receber_arquivo(self):

        self.escutar()
        cliente_conexao, cliente_endereco = self.aceitar_conexao()

        try:
            nome_arquivo = cliente_conexao.recv(1024)
            print(f'Nome do arquivo recebido')
        except:
            print('Nome do arquivo não recebido')


        try:    
            with open(f'./arquivos/{nome_arquivo.decode()}', 'wb') as arquivo:
                
                while True:
                    dado_recebido = cliente_conexao.recv(4096)

                    if dado_recebido:
                        arquivo.write(dado_recebido)
                    else:
                        break

            arquivo.close()
            print('Download do arquivo feito com sucesso')
        except:
            print('Falha ao fazer download do arquivo')


    def finalizar_conexao(self):
        self.servidor.close()


servidor: Servidor = Servidor()


servidor.escutar()
servidor.aceitar_conexao()
servidor.receber_arquivo()
servidor.finalizar_conexao()
