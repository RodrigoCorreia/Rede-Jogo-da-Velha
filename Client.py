import sys, pygame, pygame.mixer, socket

def quadrado(x, y):
	return (x/200) + (y/200)*3 + 1

def desenhaQuadrado(x, t):
	if(x == 1):
		if(t == 1):
			screen.blit(thor,(15,15))
		elif(t == 2):
			screen.blit(hulk,(15,15))
	if(x == 2):
		if(t == 1):
			screen.blit(thor,(215,15))
		elif(t == 2):
			screen.blit(hulk,(215,15))
	if(x == 3):
		if(t == 1):
			screen.blit(thor,(415,15))
		elif(t == 2):
			screen.blit(hulk,(415,15))
	if(x == 4):
		if(t == 1):
			screen.blit(thor,(15,215))
		elif(t == 2):
			screen.blit(hulk,(15,215))
	if(x == 5):
		if(t == 1):
			screen.blit(thor,(215,215))
		elif(t == 2):
			screen.blit(hulk,(215,215))
	if(x == 6):
		if(t == 1):
			screen.blit(thor,(415,215))
		elif(t == 2):
			screen.blit(hulk,(415,215))
	if(x == 7):
		if(t == 1):
			screen.blit(thor,(15,415))
		elif(t == 2):
			screen.blit(hulk,(15,415))
	if(x == 8):
		if(t == 1):
			screen.blit(thor,(215,415))
		elif(t == 2):
			screen.blit(hulk,(215,415))
	if(x == 9):
		if(t == 1):
			screen.blit(thor,(415,415))
		elif(t == 2):
			screen.blit(hulk,(415,415))

def passaTurno(t):
	if(t == 1):
		return 2
	elif(t == 2):
		return 1
		
def montaMatriz(m, x, t):
	if(x == 1):
		if(t == 1):
			m[0][0] = 1
		elif(t == 2):
			m[0][0] = 2
	if(x == 2):
		if(t == 1):
			m[0][1] = 1
		elif(t == 2):
			m[0][1] = 2
	if(x == 3):
		if(t == 1):
			m[0][2] = 1
		elif(t == 2):
			m[0][2] = 2
	if(x == 4):
		if(t == 1):
			m[1][0] = 1
		elif(t == 2):
			m[1][0] = 2
	if(x == 5):
		if(t == 1):
			m[1][1] = 1
		elif(t == 2):
			m[1][1] = 2
	if(x == 6):
		if(t == 1):
			m[1][2] = 1
		elif(t == 2):
			m[1][2] = 2
	if(x == 7):
		if(t == 1):
			m[2][0] = 1
		elif(t == 2):
			m[2][0] = 2
	if(x == 8):
		if(t == 1):
			m[2][1] = 1
		elif(t == 2):
			m[2][1] = 2
	if(x == 9):
		if(t == 1):
			m[2][2] = 1
		elif(t == 2):
			m[2][2] = 2
	return m

def validaJogada(m, x):
	if(x == 1):
		if (m[0][0] == 0):
			return True
		else: return False
	if(x == 2):
		if(m[0][1] == 0):
			return True
		else: return False
	if(x == 3):
		if(m[0][2] == 0):
			return True
		else: return False
	if(x == 4):
		if(m[1][0] ==0):
			return True
		else: return False
	if(x == 5):
		if(m[1][1] == 0):
			return True
		else: return False
	if(x == 6):
		if(m[1][2] == 0):
			return True
		else: return False
	if(x == 7):
		if(m[2][0] == 0):
			return True
		else: return False
	if(x == 8):
		if(m[2][1] == 0):
			return True
		else: return False
			
	if(x == 9):
		if(m[2][2] == 0):
			return True
		else: return False

def consultaVitoria(a):
    if a[0][0]==a[0][1]==a[0][2]== 1:
        print'jogador 1 ganhou'
        return 1
    elif a[1][0]==a[1][1]==a[1][2]== 1:
        print'jogador 1 ganhou'
        return 1
    elif a[2][0]==a[2][1]==a[2][2]== 1:
        print'jogador 1 ganhou'
        return 1
    elif a[0][0]==a[1][0]==a[2][0]== 1:
        print'jogador 1 ganhou'
        return 1
    elif a[0][1]==a[1][1]==a[2][1]== 1:
        print'jogador 1 ganhou'
        return 1
    elif a[0][2]==a[1][2]==a[2][2]== 1:
        print'jogador 1 ganhou'
        return 1
    elif a[0][0]==a[1][1]==a[2][2]== 1:
        print' jogador 1 ganhou'
        return 1
    elif a[2][0]==a[1][1]==a[0][2]== 1:
        print' jogador 1 ganhou'
        return 1
    elif a[0][0]==a[0][1]==a[0][2]== 2:
        print'jogador 2 ganhou'
        return 2
    elif a[1][0]==a[1][1]==a[1][2]== 2:
        print'jogador 2 ganhou'
        return 2
    elif a[2][0]==a[2][1]==a[2][2]== 2:
        print'jogador 2 ganhou'
        return 2
    elif a[0][0]==a[1][0]==a[2][0]== 2:
        print'jogador 2 ganhou'
        return 2
    elif a[0][1]==a[1][1]==a[2][1]== 2:
        print'jogador 2 ganhou'
        return 2
    elif a[0][2]==a[1][2]==a[2][2]== 2:
        print'jogador 2 ganhou'
        return 2
    elif a[0][0]==a[1][1]==a[2][2]== 2:
        print' jogador 2 ganhou'
        return 2
    elif a[2][0]==a[1][1]==a[0][2]== 2:
        print' jogador 2 ganhou'
        return 2
    else:
        print' jogo terminou empatado'
        return 0

def consultaEmpate(m):
	if(m[0][0] == 0):
		return False
	elif(m[0][1] == 0):
		return False
	elif(m[0][2] == 0):
		return False
	elif(m[1][0] ==0):
		return False
	elif(m[1][1] == 0):
		return False
	elif(m[1][2] == 0):
		return False
	elif(m[2][0] == 0):
		return False
	elif(m[2][1] == 0):
		return False
	elif(m[2][2] == 0):
		return False
	else: return True



#####################################inicio Jogo##########################
pygame.init()

#######################################################

host = '' 
port = 2024
addr = ((host,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
client_socket.connect(addr)
 
#mensagem = raw_input("digite uma mensagem para enviar ao servidor")
#client_socket.send(mensagem)
#reply = client_socket.recv(1024)
#print 'mensagem enviada'
#client_socket.close()

#######################################################

inicioservidor = client_socket.recv(1024) 
inicioservidor = int(inicioservidor)

conexao = 1

mat = [[0 for x in range(3)] for x in range (3)]

sound = pygame.mixer.Sound('/Music/AvengersTheme.wav')

size = width, height = 600,600

screen = pygame.display.set_mode(size)

fundo = pygame.image.load("/Images/avengers.png")
thor = pygame.image.load("/Images/Thor.png")
hulk = pygame.image.load("/Images/Hulk.png")
win = pygame.image.load("/Images/YouWin.png")
lose = pygame.image.load("/Images/YouLose.png")
drawn = pygame.image.load("/Images/DrawGame.png")

screen.blit(fundo,(0,0))
if(inicioservidor == 0):
	pygame.display.set_caption("Thor - Jogador "+ str(inicioservidor+1))
else:
	pygame.display.set_caption("Hulk - Jogador "+ str(inicioservidor+1))


pygame.display.flip()

turno = 1
continua = True
while True:

	while continua:
		aux =1
		mx,my = pygame.mouse.get_pos()
		#for event in pygame.event.get():
		#	if event.type == pygame.QUIT:
		#		sys.exit()
		#		client_socket.close()
		#	elif event.type == pygame.MOUSEBUTTONDOWN:
		if(turno == 1):
			if(inicioservidor == 0):
				########################
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
						client_socket.close()
					elif event.type == pygame.MOUSEBUTTONDOWN:

						while aux:
							captura = quadrado(mx,my)
							if(validaJogada(mat,captura)):
								aux = 0
					
						client_socket.send(str (captura))
					
						desenhaQuadrado(captura, turno)
						mat = montaMatriz(mat,captura,turno)
						turno = passaTurno(turno)
						if(consultaVitoria(mat) == 1 or consultaVitoria(mat) == 2 or consultaEmpate(mat)):
							print mat
							continua = False
				########################
			elif(inicioservidor == 1):
								
				captura = client_socket.recv(1024)
				captura = int(captura)
					
				desenhaQuadrado(captura, turno)
				mat = montaMatriz(mat,captura,turno)
				turno = passaTurno(turno)
				if(consultaVitoria(mat) == 1 or consultaVitoria(mat) == 2 or consultaEmpate(mat)):
					print mat
					continua = False
		elif(turno == 2):
			if(inicioservidor == 0):
				captura = client_socket.recv(1024)
				captura = int(captura)
						
				desenhaQuadrado(captura, turno)
				mat = montaMatriz(mat,captura,turno)
				turno = passaTurno(turno)
				if(consultaVitoria(mat) == 1 or consultaVitoria(mat) == 2 or consultaEmpate(mat)):
					print mat
					continua = False
			
			elif(inicioservidor == 1):	
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
						client_socket.close()
					elif event.type == pygame.MOUSEBUTTONDOWN:

						while aux:
							captura = quadrado(mx,my)
							if(validaJogada(mat,captura)):
								aux = 0
						
						client_socket.send(str (captura))
						
						desenhaQuadrado(captura, turno)
						mat = montaMatriz(mat,captura,turno)
						turno = passaTurno(turno)
						if(consultaVitoria(mat) == 1 or consultaVitoria(mat) == 2 or consultaEmpate(mat)):
							print mat
							continua = False			

				
		sound.play()

		pygame.display.flip()
	
	continua = True
	
	if(inicioservidor == 0):
		if(consultaVitoria(mat) == 1):
			screen.blit(win,(200,200))
		elif(consultaVitoria(mat) == 2):
			screen.blit(lose,(200,200))
		elif(consultaEmpate(mat)):
				screen.blit(drawn,(200,200))

	elif(inicioservidor == 1):
		if(consultaVitoria(mat) == 1):
			screen.blit(lose,(200,200))
		elif(consultaVitoria(mat) == 2):
			screen.blit(win,(200,200))
		elif(consultaEmpate(mat)):
				screen.blit(drawn,(200,200))
		
	leave_while = False
	pygame.display.flip()
	
	#pygame.mixer.quit()
	
	#myMovie = pygame.movie.Movie('delta.mpg')   #Load video file
	#if myMovie.has_video():
	#	resolution = myMovie.get_size()              #Get it's dimensions
	#	movie_length = myMovie.get_length()          #Get it's play length

	#	image_surface = pygame.Surface(resolution)   #Create surface for the video
	#	image_surface.fill([0,0,0])                       #Fill surface black
    #
	#	myMovie.set_display(image_surface)           #Assign video stream to the surface
	#	myMovie.play()                                    #Start video stream 	
	
	while True:	
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				client_socket.close()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
		
				screen.blit(fundo,(0,0))	
				pygame.display.flip()
				mat = [[0 for x in range(3)] for x in range (3)]
				leave_while = True
		if leave_while:
			break
