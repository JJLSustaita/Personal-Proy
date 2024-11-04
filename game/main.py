import pygame

# Inicializa pygame
pygame.init()

# Configuración de pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi Novela Visual")

# Colores y fuentes
white = (255, 255, 255)
font = pygame.font.Font(None, 32)

# Variables de historia
current_scene = "inicio"
dialogo = {
    "inicio": ["Hola, bienvenido a esta historia.", "¿Cómo te gustaría continuar?"],
    "decision_1": ["Elegiste la primera opción.", "Este es el resultado de esa decisión."],
    "decision_2": ["Elegiste la segunda opción.", "Este es otro resultado diferente."]
}
opciones = {
    "inicio": [("Opción 1", "decision_1"), ("Opción 2", "decision_2")]
}

# Ciclo principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Detectar clic en las opciones
            if current_scene in opciones:
                # Revisar cada opción y sus posiciones en pantalla
                y_offset = 130  # Ajustar este valor para que coincida con las opciones mostradas
                for idx, (text, next_scene) in enumerate(opciones[current_scene]):
                    option_rect = pygame.Rect(50, y_offset, 300, 30)  # Área de clic de cada opción
                    if option_rect.collidepoint(x, y):
                        current_scene = next_scene  # Cambiar de escena según la opción
                        break
                    y_offset += 40  # Ajustar la posición de cada opción

    # Dibujar el diálogo actual
    screen.fill(white)
    y_offset = 50
    for line in dialogo[current_scene]:
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (50, y_offset))
        y_offset += 40

    # Mostrar opciones si están disponibles
    if current_scene in opciones:
        y_offset += 20
        for idx, (text, next_scene) in enumerate(opciones[current_scene]):
            opcion_text = font.render(f"{idx + 1}. {text}", True, (0, 0, 0))
            screen.blit(opcion_text, (50, y_offset))
            y_offset += 40

    pygame.display.flip()

pygame.quit()
