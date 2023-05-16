import socket
import os

class Servidor() :

    def __init__(self, ip:str = 'localhost', porta:int = 4000):

        self.ip = ip
        self.porta = porta
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        


    def escutar(self, qt:int = 1):
        self.servidor.bind(('localhost', 4000))
        self.servidor.listen(qt)



    def aceitar_conexao(self):
        return self.servidor.accept()



    def receber_arquivo(self):
        cliente_conexao, cliente_endereco = self.aceitar_conexao()
        nome_arquivo = cliente_conexao.recv(1024)


        with open(f'./arquivos/{nome_arquivo.decode()}', 'wb') as arquivo:

            while True:
                dado_recebido = cliente_conexao.recv(10**6)

                print(dado_recebido)

                if dado_recebido:
                    arquivo.write(dado_recebido)
                else:
                    break



    def finalizar_conexao(self):
        self.servidor.close()


servidor: Servidor = Servidor()

servidor.escutar()
servidor.aceitar_conexao()
servidor.receber_arquivo()
servidor.finalizar_conexao()