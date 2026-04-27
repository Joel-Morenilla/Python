
import random
import sys

# Inicializar pygame
pygame.init()

# --- Configuración básica ---
ANCHO = 400
ALTO = 600
FPS = 60

# Colores
BLANCO = (255, 255, 255)
AZUL = (135, 206, 250)
VERDE = (0, 200, 0)

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Flappy Bird - Python Edition")
reloj = pygame.time.Clock()

# --- Cargar imágenes ---
# Puedes reemplazar estos con tus propias imágenes (32x24 px aprox)
bird_img = pygame.Surface((34, 24))
bird_img.fill((255, 255, 0))  # Amarillo para el pájaro

# Variables del pájaro
bird_x = 50
bird_y = ALTO // 2
bird_vel = 0
gravedad = 0.6
salto = -10

# Tubos
tubo_ancho = 70
tubo_espacio = 150
tubos = []
tubo_vel = 4

# Puntuación
puntaje = 0
fuente = pygame.font.SysFont(None, 36)

def crear_tubo():
    """Crea un nuevo par de tubos con una brecha aleatoria."""
    altura = random.randint(100, 400)
    tubo_superior = pygame.Rect(ANCHO, 0, tubo_ancho, altura - tubo_espacio // 2)
    tubo_inferior = pygame.Rect(ANCHO, altura + tubo_espacio // 2, tubo_ancho, ALTO)
    return tubo_superior, tubo_inferior

# Crear los primeros tubos
tubos.extend(crear_tubo())

# --- Bucle principal ---
ejecutando = True
while ejecutando:
    reloj.tick(FPS)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = salto

    # Movimiento del pájaro
    bird_vel += gravedad
    bird_y += bird_vel

    # Movimiento de tubos
    for t in tubos:
        t.x -= tubo_vel

    # Añadir nuevos tubos
    if tubos[-1].x < ANCHO - 200:
        tubos.extend(crear_tubo())

    # Eliminar tubos fuera de pantalla
    if tubos[0].x < -tubo_ancho:
        tubos.pop(0)
        tubos.pop(0)
        puntaje += 1

    # Colisiones
    bird_rect = pygame.Rect(bird_x, bird_y, 34, 24)
    for t in tubos:
        if bird_rect.colliderect(t):
            ejecutando = False

    if bird_y > ALTO or bird_y < 0:
        ejecutando = False

    # --- Dibujar todo ---
    pantalla.fill(AZUL)

    # Dibujar tubos
    for t in tubos:
        pygame.draw.rect(pantalla, VERDE, t)

    # Dibujar pájaro
    pantalla.blit(bird_img, (bird_x, bird_y))

    # Dibujar puntaje
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()