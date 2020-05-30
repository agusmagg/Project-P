import pygame

#inicializo pygame
pygame.init()


#creo la pantalla
screen = pygame.display.set_mode((800,600))  # aca pongo el ancho y alto de la ventana


#titulo e icono de ventana
pygame.display.set_caption("projectp")  # aca pongo el nombre de la ventana
icon= pygame.image.load('war.png')  # aca pongo el nombre del archivo del icono
pygame.display.set_icon(icon)


#creo el loop del programa
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # aca le estoy diciendo si aprento la x pare cerrar cambie el valor de running
            running = False

#relleno fondo pantalla RGB - Red,Gren,Blue

screen.fill((192,192,192))
pygame.display.update()
