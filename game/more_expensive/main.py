import pygame
import pandas as pd
import random
import os

class Game:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.level = 1
        self.load_data()
        self.load_images()
        self.current_choices = []

    def load_data(self):
        # Cargar datos desde el archivo Excel
        self.data = pd.read_excel('game/resources/files/objetos.xlsx')
        self.data['Precio'] = self.data['Precio ($)'].apply(lambda x: int(str(x).replace(',', '')))

    def load_images(self):
        # Cargar imágenes de la carpeta "images"
        self.images = {}
        for _, row in self.data.iterrows():
            nombre = row['Objeto']
            try:
                # Buscar el archivo de imagen en la carpeta images
                image_path = f"game/resources/images/{nombre}.jpg"
                if os.path.exists(image_path):  # Solo cargar si la imagen existe
                    image = pygame.image.load(image_path)
                    self.images[nombre] = pygame.transform.scale(image, (200, 200))
                else:
                    print(f"Imagen no encontrada para '{nombre}', omitiendo...")
            except Exception as e:
                print(f"Error cargando imagen para {nombre}: {e}")


    def get_random_choices(self):
        # Selección aleatoria de dos objetos sin repetición
        self.current_choices = random.sample(list(self.data.iterrows()), 2)

    def draw_options(self):
        # Dibujar opciones en la pantalla
        self.screen.fill((255, 255, 255))  # Fondo blanco

        # Posiciones para las imágenes y botones
        x1, y1 = 200, 200
        x2, y2 = 600, 200

        # Primer objeto
        obj1 = self.current_choices[0][1]
        img1 = self.images.get(obj1['Objeto'], None)
        
        # Dibujar imagen o cuadro vacío si no existe
        if img1:
            self.screen.blit(img1, (x1, y1))
        else:
            pygame.draw.rect(self.screen, (200, 200, 200), (x1, y1, 200, 200))  # Cuadro gris como marcador de posición

        # Mostrar nombre del objeto debajo de la imagen o cuadro vacío
        self.draw_text(obj1['Objeto'], self.font, (0, 0, 0), self.screen, x1 + 100, y1 + 220)

        # Dibujar botón
        pygame.draw.rect(self.screen, (0, 255, 0), (x1, y1 + 250, 200, 50))  # Botón
        self.draw_text("Elegir", self.font, (255, 255, 255), self.screen, x1 + 100, y1 + 275)

        # Segundo objeto
        obj2 = self.current_choices[1][1]
        img2 = self.images.get(obj2['Objeto'], None)
        
        # Dibujar imagen o cuadro vacío si no existe
        if img2:
            self.screen.blit(img2, (x2, y2))
        else:
            pygame.draw.rect(self.screen, (200, 200, 200), (x2, y2, 200, 200))  # Cuadro gris como marcador de posición

        # Mostrar nombre del objeto debajo de la imagen o cuadro vacío
        self.draw_text(obj2['Objeto'], self.font, (0, 0, 0), self.screen, x2 + 100, y2 + 220)

        # Dibujar botón
        pygame.draw.rect(self.screen, (0, 255, 0), (x2, y2 + 250, 200, 50))  # Botón
        self.draw_text("Elegir", self.font, (255, 255, 255), self.screen, x2 + 100, y2 + 275)

        # Mostrar nivel actual
        self.draw_text(f"Nivel: {self.level}", self.font, (0, 0, 0), self.screen, 400, 50)


    def check_choice(self, x, y):
        # Verificar cuál botón fue presionado
        obj1, obj2 = self.current_choices[0][1], self.current_choices[1][1]
        price1, price2 = obj1['Precio'], obj2['Precio']

        if 200 < x < 400 and 420 < y < 470:  # Botón del primer objeto
            return price1 >= price2
        elif 600 < x < 800 and 420 < y < 470:  # Botón del segundo objeto
            return price2 >= price1
        return None

    def draw_text(self, text, font, color, surface, x, y):
        # Función para mostrar texto en pantalla
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    def run(self):
        # Lógica principal del juego
        self.get_random_choices()
        self.draw_options()
        pygame.display.flip()

        waiting_for_choice = True
        while waiting_for_choice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    result = self.check_choice(x, y)
                    if result is not None:
                        waiting_for_choice = False
                        if result:
                            # Elección correcta, subir de nivel
                            self.level += 1
                        else:
                            # Elección incorrecta, reiniciar nivel
                            self.level = 1
                        self.run()

# Función principal para inicializar el juego
def main():
    # Inicializar Pygame
    pygame.init()
    
    # Configuración de la ventana
    screen_width, screen_height = 1000, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("¿Cuál objeto es más caro?")
    
    # Configuración de la fuente
    font = pygame.font.Font(None, 36)
    
    # Crear una instancia del juego y ejecutar
    game = Game(screen, font)
    game.run()

if __name__ == "__main__":
    main()
