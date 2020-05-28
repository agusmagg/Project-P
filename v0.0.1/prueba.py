import pygame



#inicializo pygame
pygame.init()


#creo la pantalla
screen = pygame.display.set_mode((800,600))  # aca pongo el ancho y alto de la ventana


#creo el loop del programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # aca le estoy diciendo si aprento la x pare cerrar cambie el valor de running
            running = FALSE
