import socket
import os

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



servidor.bind(('localhost', 4000))
servidor.listen(1)

cliente_conexao, cliente_endereco = servidor.accept()

nome_arquivo = f'./arquivos/{ cliente_conexao.recv(1024).decode() }'

print(cliente_conexao, cliente_endereco, nome_arquivo)


if os.path.isfile(nome_arquivo):

    if os.stat(nome_arquivo) >= 31.25:
        
        with open(nome_arquivo, 'wb') as arquivo:

            for dados in arquivo.readlines():
                cliente_conexao.send(dados)
            
            print('Arquivo enviado para o cliente')

    else:
        print('Arquivo menor que o esperado')
        cliente_conexao.send('Arquivo menor que o esperado'.encode())

else:
    print('Arquivo não encontrado no servidor')
    cliente_conexao.send('Arquivo nao encontrado no servidor'.encode())
