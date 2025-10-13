"""
JUEGO EDUCATIVO DE MATEMÁTICAS DISCRETAS - Versión GUI
Curso: MATH-112
Autor: Sistema Educativo Interactivo

Este juego cubre los siguientes temas de Matemáticas Discretas:
1. Aritmética Modular y Criptografía (Cifrado César)
2. Combinatoria (Permutaciones y Combinaciones)
3. Teoría de Grafos (Caminos más cortos)
4. Relaciones (Propiedades: reflexiva, simétrica, transitiva)

Características:
- Interfaz gráfica moderna con animaciones
- Retroalimentación visual inmediata
- Sistema de puntuación y progreso
- Efectos de partículas y transiciones suaves
"""

import pygame
import random
import math
import sys
from typing import List, Tuple, Optional

# Inicializar Pygame
pygame.init()

# Constantes de pantalla
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Paleta de colores moderna (inspirada en diseño tech)
COLORS = {
    'bg_dark': (10, 14, 26),
    'bg_medium': (26, 31, 53),
    'bg_light': (40, 45, 70),
    'primary': (0, 217, 255),  # Cyan brillante
    'secondary': (139, 92, 246),  # Purple
    'accent': (168, 139, 250),  # Light purple
    'success': (16, 185, 129),  # Green
    'error': (239, 68, 68),  # Red
    'warning': (251, 191, 36),  # Yellow
    'text': (255, 255, 255),
    'text_dim': (156, 163, 175),
    'border': (75, 85, 99),
}

# Configuración de fuentes
pygame.font.init()
FONT_TITLE = pygame.font.Font(None, 72)
FONT_HEADING = pygame.font.Font(None, 48)
FONT_BODY = pygame.font.Font(None, 32)
FONT_SMALL = pygame.font.Font(None, 24)

class Particle:
    """Partícula para efectos visuales"""
    def __init__(self, x: float, y: float, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-5, -1)
        self.color = color
        self.life = 1.0
        self.size = random.randint(3, 8)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.2  # Gravedad
        self.life -= 0.02
        return self.life > 0
    
    def draw(self, screen):
        alpha = int(255 * self.life)
        color_with_alpha = (*self.color, alpha)
        size = int(self.size * self.life)
        if size > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), size)

class Button:
    """Botón animado con efectos hover"""
    def __init__(self, x: int, y: int, width: int, height: int, text: str, 
                 color: Tuple[int, int, int], hover_color: Tuple[int, int, int]):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.is_hovered = False
        self.scale = 1.0
        self.target_scale = 1.0
    
    def update(self, mouse_pos: Tuple[int, int]):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.target_scale = 1.05 if self.is_hovered else 1.0
        
        # Animación suave de escala
        self.scale += (self.target_scale - self.scale) * 0.2
        
        # Transición de color suave
        target_color = self.hover_color if self.is_hovered else self.color
        self.current_color = tuple(
            int(self.current_color[i] + (target_color[i] - self.current_color[i]) * 0.2)
            for i in range(3)
        )
    
    def draw(self, screen):
        # Calcular rectángulo escalado
        scaled_width = int(self.rect.width * self.scale)
        scaled_height = int(self.rect.height * self.scale)
        scaled_x = self.rect.centerx - scaled_width // 2
        scaled_y = self.rect.centery - scaled_height // 2
        scaled_rect = pygame.Rect(scaled_x, scaled_y, scaled_width, scaled_height)
        
        # Sombra
        shadow_rect = scaled_rect.copy()
        shadow_rect.y += 4
        pygame.draw.rect(screen, (0, 0, 0, 50), shadow_rect, border_radius=12)
        
        # Botón principal
        pygame.draw.rect(screen, self.current_color, scaled_rect, border_radius=12)
        
        # Borde brillante si está hover
        if self.is_hovered:
            pygame.draw.rect(screen, COLORS['primary'], scaled_rect, 3, border_radius=12)
        
        # Texto
        text_surface = FONT_BODY.render(self.text, True, COLORS['text'])
        text_rect = text_surface.get_rect(center=scaled_rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, mouse_pos: Tuple[int, int], mouse_pressed: bool) -> bool:
        return self.rect.collidepoint(mouse_pos) and mouse_pressed

class Card:
    """Tarjeta animada para módulos del juego"""
    def __init__(self, x: int, y: int, width: int, height: int, title: str, 
                 description: str, icon: str, color: Tuple[int, int, int]):
        self.rect = pygame.Rect(x, y, width, height)
        self.title = title
        self.description = description
        self.icon = icon
        self.color = color
        self.is_hovered = False
        self.hover_offset = 0
        self.target_offset = 0
    
    def update(self, mouse_pos: Tuple[int, int]):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.target_offset = -10 if self.is_hovered else 0
        self.hover_offset += (self.target_offset - self.hover_offset) * 0.2
    
    def draw(self, screen):
        # Rectángulo con offset
        draw_rect = self.rect.copy()
        draw_rect.y += int(self.hover_offset)
        
        # Sombra
        shadow_rect = draw_rect.copy()
        shadow_rect.y += 8
        pygame.draw.rect(screen, (0, 0, 0, 30), shadow_rect, border_radius=16)
        
        # Fondo de la tarjeta
        pygame.draw.rect(screen, COLORS['bg_medium'], draw_rect, border_radius=16)
        
        # Borde brillante si está hover
        if self.is_hovered:
            pygame.draw.rect(screen, self.color, draw_rect, 3, border_radius=16)
        
        # Icono (emoji grande)
        icon_surface = FONT_HEADING.render(self.icon, True, self.color)
        icon_rect = icon_surface.get_rect(center=(draw_rect.centerx, draw_rect.top + 60))
        screen.blit(icon_surface, icon_rect)
        
        # Título
        title_surface = FONT_BODY.render(self.title, True, COLORS['text'])
        title_rect = title_surface.get_rect(center=(draw_rect.centerx, draw_rect.top + 120))
        screen.blit(title_surface, title_rect)
        
        # Descripción (multi-línea)
        words = self.description.split()
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            test_line = ' '.join(current_line)
            if FONT_SMALL.size(test_line)[0] > draw_rect.width - 40:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        
        y_offset = draw_rect.top + 160
        for line in lines[:3]:  # Máximo 3 líneas
            desc_surface = FONT_SMALL.render(line, True, COLORS['text_dim'])
            desc_rect = desc_surface.get_rect(center=(draw_rect.centerx, y_offset))
            screen.blit(desc_surface, desc_rect)
            y_offset += 30
    
    def is_clicked(self, mouse_pos: Tuple[int, int], mouse_pressed: bool) -> bool:
        return self.rect.collidepoint(mouse_pos) and mouse_pressed

class ProgressBar:
    """Barra de progreso animada"""
    def __init__(self, x: int, y: int, width: int, height: int, max_value: int):
        self.rect = pygame.Rect(x, y, width, height)
        self.max_value = max_value
        self.current_value = 0
        self.display_value = 0.0
    
    def set_value(self, value: int):
        self.current_value = min(value, self.max_value)
    
    def update(self):
        # Animación suave
        target = self.current_value / self.max_value
        self.display_value += (target - self.display_value) * 0.1
    
    def draw(self, screen):
        # Fondo
        pygame.draw.rect(screen, COLORS['bg_light'], self.rect, border_radius=8)
        
        # Barra de progreso
        fill_width = int(self.rect.width * self.display_value)
        if fill_width > 0:
            fill_rect = pygame.Rect(self.rect.x, self.rect.y, fill_width, self.rect.height)
            pygame.draw.rect(screen, COLORS['primary'], fill_rect, border_radius=8)
        
        # Borde
        pygame.draw.rect(screen, COLORS['border'], self.rect, 2, border_radius=8)
        
        # Texto de porcentaje
        percentage = int(self.display_value * 100)
        text = f"{percentage}%"
        text_surface = FONT_SMALL.render(text, True, COLORS['text'])
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class DiscreteMatGame:
    """Clase principal del juego"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Matemáticas Discretas - Juego Educativo")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Estados del juego
        self.state = "menu"  # menu, module_select, playing, results
        self.current_module = None
        
        # Puntuación
        self.score = 0
        self.total_questions = 0
        self.correct_answers = 0
        
        # Partículas
        self.particles: List[Particle] = []
        
        # Animación de fondo
        self.bg_offset = 0
        
        # Inicializar módulos
        self.init_modules()
    
    def init_modules(self):
        """Inicializar tarjetas de módulos"""
        card_width = 250
        card_height = 280
        spacing = 30
        start_x = (SCREEN_WIDTH - (card_width * 4 + spacing * 3)) // 2
        start_y = 200
        
        self.module_cards = [
            Card(start_x, start_y, card_width, card_height,
                 "Criptografía", "Descifra mensajes con aritmética modular",
                 "🔐", COLORS['primary']),
            Card(start_x + card_width + spacing, start_y, card_width, card_height,
                 "Combinatoria", "Resuelve problemas de permutaciones",
                 "🎲", COLORS['secondary']),
            Card(start_x + (card_width + spacing) * 2, start_y, card_width, card_height,
                 "Grafos", "Encuentra caminos más cortos",
                 "🗺️", COLORS['success']),
            Card(start_x + (card_width + spacing) * 3, start_y, card_width, card_height,
                 "Relaciones", "Identifica propiedades matemáticas",
                 "🔗", COLORS['warning']),
        ]
        
        # Botón de regreso
        self.back_button = Button(50, SCREEN_HEIGHT - 80, 150, 50,
                                   "← Volver", COLORS['bg_light'], COLORS['bg_medium'])
    
    def draw_background(self):
        """Dibujar fondo animado con patrón geométrico"""
        self.screen.fill(COLORS['bg_dark'])
        
        # Patrón de líneas animadas
        self.bg_offset += 0.5
        if self.bg_offset > 50:
            self.bg_offset = 0
        
        for i in range(0, SCREEN_WIDTH + 100, 50):
            x = i - self.bg_offset
            pygame.draw.line(self.screen, COLORS['bg_medium'], 
                           (x, 0), (x - 100, SCREEN_HEIGHT), 1)
        
        for i in range(0, SCREEN_HEIGHT + 100, 50):
            y = i - self.bg_offset
            pygame.draw.line(self.screen, COLORS['bg_medium'],
                           (0, y), (SCREEN_WIDTH, y - 100), 1)
    
    def draw_menu(self):
        """Dibujar menú principal"""
        # Título con efecto de brillo
        title_text = "MATEMÁTICAS DISCRETAS"
        title_surface = FONT_TITLE.render(title_text, True, COLORS['primary'])
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 150))
        
        # Sombra del título
        shadow_surface = FONT_TITLE.render(title_text, True, COLORS['bg_medium'])
        shadow_rect = shadow_surface.get_rect(center=(SCREEN_WIDTH // 2 + 4, 154))
        self.screen.blit(shadow_surface, shadow_rect)
        self.screen.blit(title_surface, title_rect)
        
        # Subtítulo
        subtitle = "Juego Educativo Interactivo"
        subtitle_surface = FONT_BODY.render(subtitle, True, COLORS['text_dim'])
        subtitle_rect = subtitle_surface.get_rect(center=(SCREEN_WIDTH // 2, 220))
        self.screen.blit(subtitle_surface, subtitle_rect)
        
        # Botón de inicio
        start_button = Button(SCREEN_WIDTH // 2 - 150, 350, 300, 70,
                             "COMENZAR", COLORS['primary'], COLORS['accent'])
        mouse_pos = pygame.mouse.get_pos()
        start_button.update(mouse_pos)
        start_button.draw(self.screen)
        
        # Información del curso
        info_text = "Curso: MATH-112 | Universidad"
        info_surface = FONT_SMALL.render(info_text, True, COLORS['text_dim'])
        info_rect = info_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.screen.blit(info_surface, info_rect)
        
        # Detectar clic
        if pygame.mouse.get_pressed()[0]:
            if start_button.is_clicked(mouse_pos, True):
                self.state = "module_select"
                self.spawn_particles(SCREEN_WIDTH // 2, 385, COLORS['primary'])
                pygame.time.wait(100)
    
    def draw_module_select(self):
        """Dibujar selección de módulos"""
        # Título
        title = "Selecciona un Módulo"
        title_surface = FONT_HEADING.render(title, True, COLORS['text'])
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title_surface, title_rect)
        
        # Actualizar y dibujar tarjetas
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        
        for i, card in enumerate(self.module_cards):
            card.update(mouse_pos)
            card.draw(self.screen)
            
            if card.is_clicked(mouse_pos, mouse_pressed):
                self.current_module = i
                self.state = "playing"
                self.init_game_module(i)
                self.spawn_particles(card.rect.centerx, card.rect.centery, card.color)
                pygame.time.wait(100)
        
        # Botón de regreso
        self.back_button.update(mouse_pos)
        self.back_button.draw(self.screen)
        
        if self.back_button.is_clicked(mouse_pos, mouse_pressed):
            self.state = "menu"
            pygame.time.wait(100)
    
    def init_game_module(self, module_index: int):
        """Inicializar módulo de juego específico"""
        self.score = 0
        self.total_questions = 0
        self.correct_answers = 0
        self.current_question = 0
        self.max_questions = 5
        
        if module_index == 0:  # Criptografía
            self.init_crypto_module()
        elif module_index == 1:  # Combinatoria
            self.init_combinatorics_module()
        elif module_index == 2:  # Grafos
            self.init_graph_module()
        elif module_index == 3:  # Relaciones
            self.init_relations_module()
    
    def init_crypto_module(self):
        """Inicializar módulo de criptografía"""
        self.module_name = "Criptografía - Cifrado César"
        self.module_color = COLORS['primary']
        self.generate_crypto_question()
    
    def generate_crypto_question(self):
        """Generar pregunta de criptografía"""
        messages = ["HOLA", "PYTHON", "MATEMATICAS", "DISCRETAS", "CIFRADO"]
        self.original_message = random.choice(messages)
        self.shift = random.randint(1, 25)
        
        # Cifrar mensaje usando aritmética modular
        self.encrypted_message = ""
        for char in self.original_message:
            if char.isalpha():
                # Aplicar: c = (m + k) mod 26
                shifted = (ord(char) - ord('A') + self.shift) % 26
                self.encrypted_message += chr(shifted + ord('A'))
            else:
                self.encrypted_message += char
        
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = COLORS['text_dim']
    
    def init_combinatorics_module(self):
        """Inicializar módulo de combinatoria"""
        self.module_name = "Combinatoria"
        self.module_color = COLORS['secondary']
        self.generate_combinatorics_question()
    
    def generate_combinatorics_question(self):
        """Generar pregunta de combinatoria"""
        self.problem_type = random.choice(["permutation", "combination"])
        
        if self.problem_type == "permutation":
            self.n = random.randint(5, 10)
            self.r = random.randint(2, min(5, self.n))
            # P(n,r) = n! / (n-r)!
            self.correct_answer = self.factorial(self.n) // self.factorial(self.n - self.r)
            self.question = f"¿De cuántas formas se pueden ordenar {self.r} elementos de un conjunto de {self.n}?"
            self.formula = f"P({self.n},{self.r}) = {self.n}! / ({self.n}-{self.r})!"
        else:
            self.n = random.randint(5, 10)
            self.r = random.randint(2, min(5, self.n))
            # C(n,r) = n! / (r! * (n-r)!)
            self.correct_answer = self.factorial(self.n) // (self.factorial(self.r) * self.factorial(self.n - self.r))
            self.question = f"¿De cuántas formas se pueden elegir {self.r} elementos de un conjunto de {self.n}?"
            self.formula = f"C({self.n},{self.r}) = {self.n}! / ({self.r}! × ({self.n}-{self.r})!)"
        
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = COLORS['text_dim']
    
    def factorial(self, n: int) -> int:
        """Calcular factorial"""
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)
    
    def init_graph_module(self):
        """Inicializar módulo de grafos"""
        self.module_name = "Teoría de Grafos"
        self.module_color = COLORS['success']
        self.generate_graph_question()
    
    def generate_graph_question(self):
        """Generar pregunta de grafos"""
        # Crear un grafo simple con 4 nodos
        self.graph = {
            'A': {'B': random.randint(1, 9), 'C': random.randint(1, 9)},
            'B': {'A': 0, 'C': random.randint(1, 9), 'D': random.randint(1, 9)},
            'C': {'A': 0, 'B': 0, 'D': random.randint(1, 9)},
            'D': {'B': 0, 'C': 0}
        }
        # Hacer simétrico
        self.graph['A']['B'] = self.graph['B']['A'] = random.randint(1, 9)
        self.graph['A']['C'] = self.graph['C']['A'] = random.randint(1, 9)
        self.graph['B']['C'] = self.graph['C']['B'] = random.randint(1, 9)
        self.graph['B']['D'] = self.graph['D']['B'] = random.randint(1, 9)
        self.graph['C']['D'] = self.graph['D']['C'] = random.randint(1, 9)
        
        # Calcular camino más corto de A a D usando algoritmo simple
        path1 = self.graph['A']['B'] + self.graph['B']['D']
        path2 = self.graph['A']['C'] + self.graph['C']['D']
        path3 = self.graph['A']['B'] + self.graph['B']['C'] + self.graph['C']['D']
        
        self.correct_answer = min(path1, path2, path3)
        self.user_input = ""
        self.feedback = ""
        self.feedback_color = COLORS['text_dim']
    
    def init_relations_module(self):
        """Inicializar módulo de relaciones"""
        self.module_name = "Relaciones"
        self.module_color = COLORS['warning']
        self.generate_relations_question()
    
    def generate_relations_question(self):
        """Generar pregunta de relaciones"""
        self.relation_types = [
            ("Reflexiva", "Todo elemento está relacionado consigo mismo"),
            ("Simétrica", "Si a~b entonces b~a"),
            ("Transitiva", "Si a~b y b~c entonces a~c")
        ]
        
        self.correct_property = random.choice(self.relation_types)
        
        # Generar conjunto y relación
        self.set_elements = ['a', 'b', 'c', 'd']
        
        if self.correct_property[0] == "Reflexiva":
            self.relation = [(x, x) for x in self.set_elements]
            self.relation.extend([('a', 'b'), ('b', 'c')])
        elif self.correct_property[0] == "Simétrica":
            self.relation = [('a', 'b'), ('b', 'a'), ('c', 'd'), ('d', 'c')]
        else:  # Transitiva
            self.relation = [('a', 'b'), ('b', 'c'), ('a', 'c')]
        
        random.shuffle(self.relation)
        
        self.user_answer = None
        self.feedback = ""
        self.feedback_color = COLORS['text_dim']
        
        # Botones de opciones
        self.option_buttons = []
        button_y = 400
        for i, (prop, desc) in enumerate(self.relation_types):
            btn = Button(SCREEN_WIDTH // 2 - 200, button_y + i * 80, 400, 60,
                        prop, COLORS['bg_light'], COLORS['bg_medium'])
            self.option_buttons.append(btn)
    
    def draw_playing(self):
        """Dibujar pantalla de juego"""
        # Encabezado con nombre del módulo
        header_rect = pygame.Rect(0, 0, SCREEN_WIDTH, 80)
        pygame.draw.rect(self.screen, COLORS['bg_medium'], header_rect)
        pygame.draw.line(self.screen, self.module_color, (0, 80), (SCREEN_WIDTH, 80), 3)
        
        title_surface = FONT_HEADING.render(self.module_name, True, self.module_color)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 40))
        self.screen.blit(title_surface, title_rect)
        
        # Barra de progreso
        progress_bar = ProgressBar(50, 100, 300, 30, self.max_questions)
        progress_bar.set_value(self.current_question)
        progress_bar.update()
        progress_bar.draw(self.screen)
        
        # Puntuación
        score_text = f"Puntos: {self.score}"
        score_surface = FONT_BODY.render(score_text, True, COLORS['primary'])
        score_rect = score_surface.get_rect(topright=(SCREEN_WIDTH - 50, 100))
        self.screen.blit(score_surface, score_rect)
        
        # Dibujar contenido específico del módulo
        if self.current_module == 0:
            self.draw_crypto_game()
        elif self.current_module == 1:
            self.draw_combinatorics_game()
        elif self.current_module == 2:
            self.draw_graph_game()
        elif self.current_module == 3:
            self.draw_relations_game()
        
        # Botón de regreso
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.update(mouse_pos)
        self.back_button.draw(self.screen)
        
        if self.back_button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0]):
            self.state = "module_select"
            pygame.time.wait(100)
    
    def draw_crypto_game(self):
        """Dibujar juego de criptografía"""
        # Pregunta
        question = "Descifra el mensaje usando el cifrado César"
        question_surface = FONT_BODY.render(question, True, COLORS['text'])
        question_rect = question_surface.get_rect(center=(SCREEN_WIDTH // 2, 180))
        self.screen.blit(question_surface, question_rect)
        
        # Mensaje cifrado
        encrypted_label = FONT_SMALL.render("Mensaje Cifrado:", True, COLORS['text_dim'])
        self.screen.blit(encrypted_label, (SCREEN_WIDTH // 2 - 200, 240))
        
        encrypted_surface = FONT_HEADING.render(self.encrypted_message, True, self.module_color)
        encrypted_rect = encrypted_surface.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.screen.blit(encrypted_surface, encrypted_rect)
        
        # Pista del desplazamiento
        hint = f"Desplazamiento: {self.shift}"
        hint_surface = FONT_SMALL.render(hint, True, COLORS['warning'])
        hint_rect = hint_surface.get_rect(center=(SCREEN_WIDTH // 2, 350))
        self.screen.blit(hint_surface, hint_rect)
        
        # Fórmula
        formula = "Descifrado: m = (c - k) mod 26"
        formula_surface = FONT_SMALL.render(formula, True, COLORS['text_dim'])
        formula_rect = formula_surface.get_rect(center=(SCREEN_WIDTH // 2, 390))
        self.screen.blit(formula_surface, formula_rect)
        
        # Campo de entrada
        input_label = FONT_SMALL.render("Tu respuesta:", True, COLORS['text_dim'])
        self.screen.blit(input_label, (SCREEN_WIDTH // 2 - 200, 440))
        
        input_rect = pygame.Rect(SCREEN_WIDTH // 2 - 200, 470, 400, 50)
        pygame.draw.rect(self.screen, COLORS['bg_light'], input_rect, border_radius=8)
        pygame.draw.rect(self.screen, COLORS['border'], input_rect, 2, border_radius=8)
        
        input_surface = FONT_BODY.render(self.user_input, True, COLORS['text'])
        self.screen.blit(input_surface, (input_rect.x + 10, input_rect.y + 10))
        
        # Botón de verificar
        check_button = Button(SCREEN_WIDTH // 2 - 100, 550, 200, 50,
                             "Verificar", self.module_color, COLORS['accent'])
        mouse_pos = pygame.mouse.get_pos()
        check_button.update(mouse_pos)
        check_button.draw(self.screen)
        
        if check_button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0]):
            self.check_crypto_answer()
            pygame.time.wait(100)
        
        # Feedback
        if self.feedback:
            feedback_surface = FONT_BODY.render(self.feedback, True, self.feedback_color)
            feedback_rect = feedback_surface.get_rect(center=(SCREEN_WIDTH // 2, 630))
            self.screen.blit(feedback_surface, feedback_rect)
    
    def check_crypto_answer(self):
        """Verificar respuesta de criptografía"""
        if self.user_input.upper() == self.original_message:
            self.feedback = "¡Correcto! +100 puntos"
            self.feedback_color = COLORS['success']
            self.score += 100
            self.correct_answers += 1
            self.spawn_particles(SCREEN_WIDTH // 2, 500, COLORS['success'])
            pygame.time.wait(1000)
            self.next_question()
        else:
            self.feedback = f"Incorrecto. La respuesta era: {self.original_message}"
            self.feedback_color = COLORS['error']
            self.spawn_particles(SCREEN_WIDTH // 2, 500, COLORS['error'])
            pygame.time.wait(1500)
            self.next_question()
    
    def draw_combinatorics_game(self):
        """Dibujar juego de combinatoria"""
        # Pregunta
        question_surface = FONT_BODY.render(self.question, True, COLORS['text'])
        question_rect = question_surface.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.screen.blit(question_surface, question_rect)
        
        # Fórmula
        formula_label = FONT_SMALL.render("Fórmula:", True, COLORS['text_dim'])
        self.screen.blit(formula_label, (SCREEN_WIDTH // 2 - 200, 270))
        
        formula_surface = FONT_BODY.render(self.formula, True, self.module_color)
        formula_rect = formula_surface.get_rect(center=(SCREEN_WIDTH // 2, 320))
        self.screen.blit(formula_surface, formula_rect)
        
        # Campo de entrada
        input_label = FONT_SMALL.render("Tu respuesta:", True, COLORS['text_dim'])
        self.screen.blit(input_label, (SCREEN_WIDTH // 2 - 200, 390))
        
        input_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, 420, 300, 50)
        pygame.draw.rect(self.screen, COLORS['bg_light'], input_rect, border_radius=8)
        pygame.draw.rect(self.screen, COLORS['border'], input_rect, 2, border_radius=8)
        
        input_surface = FONT_BODY.render(self.user_input, True, COLORS['text'])
        self.screen.blit(input_surface, (input_rect.x + 10, input_rect.y + 10))
        
        # Botón de verificar
        check_button = Button(SCREEN_WIDTH // 2 - 100, 500, 200, 50,
                             "Verificar", self.module_color, COLORS['accent'])
        mouse_pos = pygame.mouse.get_pos()
        check_button.update(mouse_pos)
        check_button.draw(self.screen)
        
        if check_button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0]):
            self.check_combinatorics_answer()
            pygame.time.wait(100)
        
        # Feedback
        if self.feedback:
            feedback_surface = FONT_BODY.render(self.feedback, True, self.feedback_color)
            feedback_rect = feedback_surface.get_rect(center=(SCREEN_WIDTH // 2, 580))
            self.screen.blit(feedback_surface, feedback_rect)
    
    def check_combinatorics_answer(self):
        """Verificar respuesta de combinatoria"""
        try:
            user_answer = int(self.user_input)
            if user_answer == self.correct_answer:
                self.feedback = "¡Correcto! +100 puntos"
                self.feedback_color = COLORS['success']
                self.score += 100
                self.correct_answers += 1
                self.spawn_particles(SCREEN_WIDTH // 2, 450, COLORS['success'])
                pygame.time.wait(1000)
                self.next_question()
            else:
                self.feedback = f"Incorrecto. La respuesta era: {self.correct_answer}"
                self.feedback_color = COLORS['error']
                self.spawn_particles(SCREEN_WIDTH // 2, 450, COLORS['error'])
                pygame.time.wait(1500)
                self.next_question()
        except ValueError:
            self.feedback = "Por favor ingresa un número válido"
            self.feedback_color = COLORS['warning']
    
    def draw_graph_game(self):
        """Dibujar juego de grafos"""
        # Pregunta
        question = "¿Cuál es el camino más corto de A a D?"
        question_surface = FONT_BODY.render(question, True, COLORS['text'])
        question_rect = question_surface.get_rect(center=(SCREEN_WIDTH // 2, 180))
        self.screen.blit(question_surface, question_rect)
        
        # Dibujar grafo
        node_positions = {
            'A': (300, 300),
            'B': (500, 250),
            'C': (500, 350),
            'D': (700, 300)
        }
        
        # Dibujar aristas con pesos
        for node1, connections in self.graph.items():
            for node2, weight in connections.items():
                if weight > 0 and node1 < node2:  # Evitar duplicados
                    pos1 = node_positions[node1]
                    pos2 = node_positions[node2]
                    
                    # Línea
                    pygame.draw.line(self.screen, COLORS['border'], pos1, pos2, 3)
                    
                    # Peso en el medio
                    mid_x = (pos1[0] + pos2[0]) // 2
                    mid_y = (pos1[1] + pos2[1]) // 2
                    
                    # Círculo de fondo para el peso
                    pygame.draw.circle(self.screen, COLORS['bg_medium'], (mid_x, mid_y), 20)
                    pygame.draw.circle(self.screen, self.module_color, (mid_x, mid_y), 20, 2)
                    
                    weight_surface = FONT_SMALL.render(str(weight), True, COLORS['text'])
                    weight_rect = weight_surface.get_rect(center=(mid_x, mid_y))
                    self.screen.blit(weight_surface, weight_rect)
        
        # Dibujar nodos
        for node, pos in node_positions.items():
            # Círculo del nodo
            pygame.draw.circle(self.screen, COLORS['bg_light'], pos, 35)
            pygame.draw.circle(self.screen, self.module_color, pos, 35, 3)
            
            # Letra del nodo
            node_surface = FONT_HEADING.render(node, True, COLORS['text'])
            node_rect = node_surface.get_rect(center=pos)
            self.screen.blit(node_surface, node_rect)
        
        # Campo de entrada
        input_label = FONT_SMALL.render("Distancia más corta:", True, COLORS['text_dim'])
        self.screen.blit(input_label, (SCREEN_WIDTH // 2 - 150, 450))
        
        input_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 480, 200, 50)
        pygame.draw.rect(self.screen, COLORS['bg_light'], input_rect, border_radius=8)
        pygame.draw.rect(self.screen, COLORS['border'], input_rect, 2, border_radius=8)
        
        input_surface = FONT_BODY.render(self.user_input, True, COLORS['text'])
        self.screen.blit(input_surface, (input_rect.x + 10, input_rect.y + 10))
        
        # Botón de verificar
        check_button = Button(SCREEN_WIDTH // 2 - 100, 560, 200, 50,
                             "Verificar", self.module_color, COLORS['accent'])
        mouse_pos = pygame.mouse.get_pos()
        check_button.update(mouse_pos)
        check_button.draw(self.screen)
        
        if check_button.is_clicked(mouse_pos, pygame.mouse.get_pressed()[0]):
            self.check_graph_answer()
            pygame.time.wait(100)
        
        # Feedback
        if self.feedback:
            feedback_surface = FONT_BODY.render(self.feedback, True, self.feedback_color)
            feedback_rect = feedback_surface.get_rect(center=(SCREEN_WIDTH // 2, 640))
            self.screen.blit(feedback_surface, feedback_rect)
    
    def check_graph_answer(self):
        """Verificar respuesta de grafos"""
        try:
            user_answer = int(self.user_input)
            if user_answer == self.correct_answer:
                self.feedback = "¡Correcto! +100 puntos"
                self.feedback_color = COLORS['success']
                self.score += 100
                self.correct_answers += 1
                self.spawn_particles(SCREEN_WIDTH // 2, 505, COLORS['success'])
                pygame.time.wait(1000)
                self.next_question()
            else:
                self.feedback = f"Incorrecto. La respuesta era: {self.correct_answer}"
                self.feedback_color = COLORS['error']
                self.spawn_particles(SCREEN_WIDTH // 2, 505, COLORS['error'])
                pygame.time.wait(1500)
                self.next_question()
        except ValueError:
            self.feedback = "Por favor ingresa un número válido"
            self.feedback_color = COLORS['warning']
    
    def draw_relations_game(self):
        """Dibujar juego de relaciones"""
        # Pregunta
        question = "¿Qué propiedad tiene esta relación?"
        question_surface = FONT_BODY.render(question, True, COLORS['text'])
        question_rect = question_surface.get_rect(center=(SCREEN_WIDTH // 2, 180))
        self.screen.blit(question_surface, question_rect)
        
        # Mostrar relación
        relation_label = FONT_SMALL.render("Relación R:", True, COLORS['text_dim'])
        self.screen.blit(relation_label, (SCREEN_WIDTH // 2 - 250, 240))
        
        relation_str = "{ " + ", ".join([f"({a},{b})" for a, b in self.relation]) + " }"
        relation_surface = FONT_BODY.render(relation_str, True, self.module_color)
        relation_rect = relation_surface.get_rect(center=(SCREEN_WIDTH // 2, 290))
        self.screen.blit(relation_surface, relation_rect)
        
        # Conjunto
        set_str = f"Conjunto: {{ {', '.join(self.set_elements)} }}"
        set_surface = FONT_SMALL.render(set_str, True, COLORS['text_dim'])
        set_rect = set_surface.get_rect(center=(SCREEN_WIDTH // 2, 340))
        self.screen.blit(set_surface, set_rect)
        
        # Botones de opciones
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        
        for i, btn in enumerate(self.option_buttons):
            btn.update(mouse_pos)
            btn.draw(self.screen)
            
            if btn.is_clicked(mouse_pos, mouse_pressed):
                self.check_relations_answer(i)
                pygame.time.wait(100)
        
        # Feedback
        if self.feedback:
            feedback_surface = FONT_BODY.render(self.feedback, True, self.feedback_color)
            feedback_rect = feedback_surface.get_rect(center=(SCREEN_WIDTH // 2, 650))
            self.screen.blit(feedback_surface, feedback_rect)
    
    def check_relations_answer(self, selected_index: int):
        """Verificar respuesta de relaciones"""
        selected_property = self.relation_types[selected_index][0]
        
        if selected_property == self.correct_property[0]:
            self.feedback = f"¡Correcto! Es {self.correct_property[0]}: {self.correct_property[1]}"
            self.feedback_color = COLORS['success']
            self.score += 100
            self.correct_answers += 1
            self.spawn_particles(SCREEN_WIDTH // 2, 400 + selected_index * 80, COLORS['success'])
            pygame.time.wait(1500)
            self.next_question()
        else:
            self.feedback = f"Incorrecto. Era {self.correct_property[0]}: {self.correct_property[1]}"
            self.feedback_color = COLORS['error']
            self.spawn_particles(SCREEN_WIDTH // 2, 400 + selected_index * 80, COLORS['error'])
            pygame.time.wait(2000)
            self.next_question()
    
    def next_question(self):
        """Avanzar a la siguiente pregunta"""
        self.current_question += 1
        self.total_questions += 1
        
        if self.current_question >= self.max_questions:
            self.state = "results"
        else:
            # Generar nueva pregunta
            if self.current_module == 0:
                self.generate_crypto_question()
            elif self.current_module == 1:
                self.generate_combinatorics_question()
            elif self.current_module == 2:
                self.generate_graph_question()
            elif self.current_module == 3:
                self.generate_relations_question()
    
    def draw_results(self):
        """Dibujar pantalla de resultados"""
        # Título
        title = "¡Juego Completado!"
        title_surface = FONT_TITLE.render(title, True, COLORS['primary'])
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title_surface, title_rect)
        
        # Puntuación final
        score_text = f"Puntuación Final: {self.score}"
        score_surface = FONT_HEADING.render(score_text, True, COLORS['text'])
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 250))
        self.screen.blit(score_surface, score_rect)
        
        # Estadísticas
        accuracy = (self.correct_answers / self.total_questions * 100) if self.total_questions > 0 else 0
        stats_text = f"Respuestas correctas: {self.correct_answers}/{self.total_questions} ({accuracy:.1f}%)"
        stats_surface = FONT_BODY.render(stats_text, True, COLORS['text_dim'])
        stats_rect = stats_surface.get_rect(center=(SCREEN_WIDTH // 2, 320))
        self.screen.blit(stats_surface, stats_rect)
        
        # Mensaje de motivación
        if accuracy >= 80:
            message = "¡Excelente trabajo! Dominas el tema."
            message_color = COLORS['success']
        elif accuracy >= 60:
            message = "¡Buen trabajo! Sigue practicando."
            message_color = COLORS['primary']
        else:
            message = "Sigue intentando. La práctica hace al maestro."
            message_color = COLORS['warning']
        
        message_surface = FONT_BODY.render(message, True, message_color)
        message_rect = message_surface.get_rect(center=(SCREEN_WIDTH // 2, 380))
        self.screen.blit(message_surface, message_rect)
        
        # Botones
        retry_button = Button(SCREEN_WIDTH // 2 - 250, 480, 200, 60,
                             "Reintentar", COLORS['primary'], COLORS['accent'])
        menu_button = Button(SCREEN_WIDTH // 2 + 50, 480, 200, 60,
                            "Menú Principal", COLORS['secondary'], COLORS['accent'])
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        
        retry_button.update(mouse_pos)
        retry_button.draw(self.screen)
        
        menu_button.update(mouse_pos)
        menu_button.draw(self.screen)
        
        if retry_button.is_clicked(mouse_pos, mouse_pressed):
            self.init_game_module(self.current_module)
            self.state = "playing"
            pygame.time.wait(100)
        
        if menu_button.is_clicked(mouse_pos, mouse_pressed):
            self.state = "module_select"
            pygame.time.wait(100)
    
    def spawn_particles(self, x: int, y: int, color: Tuple[int, int, int]):
        """Generar partículas en una posición"""
        for _ in range(20):
            self.particles.append(Particle(x, y, color))
    
    def update_particles(self):
        """Actualizar y eliminar partículas muertas"""
        self.particles = [p for p in self.particles if p.update()]
    
    def draw_particles(self):
        """Dibujar todas las partículas"""
        for particle in self.particles:
            particle.draw(self.screen)
    
    def handle_events(self):
        """Manejar eventos de Pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if self.state == "playing":
                    if event.key == pygame.K_BACKSPACE:
                        self.user_input = self.user_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        # Verificar respuesta según el módulo
                        if self.current_module == 0:
                            self.check_crypto_answer()
                        elif self.current_module == 1:
                            self.check_combinatorics_answer()
                        elif self.current_module == 2:
                            self.check_graph_answer()
                    elif event.unicode.isprintable():
                        if len(self.user_input) < 20:
                            self.user_input += event.unicode.upper()
    
    def run(self):
        """Bucle principal del juego"""
        while self.running:
            self.handle_events()
            
            # Dibujar
            self.draw_background()
            
            if self.state == "menu":
                self.draw_menu()
            elif self.state == "module_select":
                self.draw_module_select()
            elif self.state == "playing":
                self.draw_playing()
            elif self.state == "results":
                self.draw_results()
            
            # Actualizar y dibujar partículas
            self.update_particles()
            self.draw_particles()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = DiscreteMatGame()
    game.run()
