import sys,Pygame

#Inicializamos Pygamep
pygame.init_()
#Ventana
size= 800,800                               # paso tamaño de la ventana
screen =pygame.display.set_mode(size)
#Titulo de la Ventana
pygame.display.set_caption("Project P")


#Bucle juego

run=True

while run:
    #Capturamos los eventos que se han producido

    for event in pygame.event.get():






        #si el evento es salir de la ventana termina
        if event.type == pygame.QUIT: run = False

#Salida
pygame.quit()
