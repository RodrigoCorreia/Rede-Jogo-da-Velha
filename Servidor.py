import socket
 
host = ''
port = 2024
 
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(2)
 
print 'aguardando conexao'

jogador1, cliente = serv_socket.accept()
print 'Jogador 1 conectado'
jogador2, cliente = serv_socket.accept()
print 'Jogador 2 conectado'

print 'Definindo cliente 1 Jogador 1'
pacote = 0
jogador1.send(str (pacote))
print 'Definindo cliente 2 Jogador 2'
pacote = 1
jogador2.send(str (pacote))
pacote = str(pacote)

again = True

while again:
	
	print 'Turno 1'
	pacote = jogador1.recv(1024)
	jogador2.send(pacote)
	print 'Jogador 1 mandou o pacote ' + pacote + ' para o jogador 2'

	print 'Turno 2'	
	pacote = jogador2.recv(1024)
	jogador1.send(pacote)
	print 'Jogador 2 mandou o pacote ' + pacote + ' para o jogador 1'
	
serv_socket.close()
