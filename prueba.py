import pygame

# Configuración inicial
pygame.init()
ventana = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

# Carga de imágenes
imagen1 = pygame.image.load(r"C:\Users\arria\OneDrive\Escritorio\caballero\Colour1\NoOutline\120x80_gifs\__Attack.gif")
imagen2 = pygame.image.load(r"C:\Users\arria\OneDrive\Escritorio\caballero\Colour1\NoOutline\120x80_gifs\__Attack2.gif")
imagenes = [imagen1, imagen2]

# Variables
x = 0
y = 0
indice = 0

# Bucle principal
while True:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Actualización de la pantalla
    ventana.blit(imagenes[indice], (x, y))
    pygame.display.flip()

    # Control de la velocidad
    reloj.tick(30)  # 30 fps

    # Cambio de imagen
    indice += 1
    if indice >= len(imagenes):
        indice = 0
