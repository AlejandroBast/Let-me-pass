"""
Juego Educativo de Matemáticas Discretas
MATH-112 - Nivel Universitario

Este juego cubre los siguientes temas:
1. Aritmética Modular y Criptografía
2. Combinatoria (Permutaciones y Combinaciones)
3. Teoría de Grafos (Caminos más cortos)
4. Relaciones (Propiedades: reflexiva, simétrica, transitiva)

Autor: v0
Propósito: Enseñar y evaluar conceptos de Matemáticas Discretas de forma interactiva
"""

import random
import math
from typing import List, Tuple, Set

class DiscreteMatGame:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        
    def clear_screen(self):
        """Limpia la pantalla (simulado con líneas)"""
        print("\n" * 2)
        print("=" * 60)
    
    def show_menu(self):
        """Muestra el menú principal del juego"""
        self.clear_screen()
        print("🎓 JUEGO EDUCATIVO DE MATEMÁTICAS DISCRETAS 🎓")
        print("=" * 60)
        print("\nSelecciona un módulo para jugar:")
        print("\n1. 🔐 Aritmética Modular y Criptografía")
        print("2. 🎲 Combinatoria (Permutaciones y Combinaciones)")
        print("3. 🗺️  Teoría de Grafos (Caminos más cortos)")
        print("4. 🔗 Relaciones (Propiedades)")
        print("5. 📊 Ver puntuación final y salir")
        print("\n" + "=" * 60)
        
    def modular_arithmetic_game(self):
        """
        TEMA: ARITMÉTICA MODULAR
        
        Concepto matemático:
        - La aritmética modular trabaja con el residuo de la división
        - a ≡ b (mod n) significa que a y b tienen el mismo residuo al dividir por n
        - Aplicación: Criptografía (cifrado César)
        
        En este juego, el jugador debe descifrar mensajes usando aritmética modular.
        """
        self.clear_screen()
        print("🔐 MÓDULO: ARITMÉTICA MODULAR Y CRIPTOGRAFÍA")
        print("=" * 60)
        print("\n📚 CONCEPTO:")
        print("El cifrado César desplaza cada letra del alfabeto n posiciones.")
        print("Matemáticamente: C = (P + k) mod 26")
        print("Donde P es la posición de la letra original y k es la clave.")
        print("\n" + "=" * 60)
        
        # Generar un mensaje simple para cifrar
        messages = ["HOLA", "MATE", "GRAFO", "LOGICA"]
        original_message = random.choice(messages)
        shift = random.randint(1, 25)
        
        # Cifrar el mensaje usando aritmética modular
        encrypted = ""
        for char in original_message:
            if char.isalpha():
                # Aplicar aritmética modular: (posición + desplazamiento) mod 26
                pos = ord(char) - ord('A')
                new_pos = (pos + shift) % 26
                encrypted += chr(new_pos + ord('A'))
            else:
                encrypted += char
        
        print(f"\n🔒 Mensaje cifrado: {encrypted}")
        print(f"🔑 Clave de desplazamiento: {shift}")
        print("\n❓ ¿Cuál es el mensaje original?")
        
        user_answer = input("Tu respuesta: ").upper().strip()
        
        if user_answer == original_message:
            print("\n✅ ¡CORRECTO! Has descifrado el mensaje.")
            print(f"Explicación: Cada letra se desplazó {shift} posiciones hacia atrás.")
            print(f"Fórmula usada: P = (C - {shift}) mod 26")
            self.score += 10
            self.total_questions += 1
        else:
            print(f"\n❌ Incorrecto. El mensaje era: {original_message}")
            print(f"Recuerda: Para descifrar, resta el desplazamiento módulo 26.")
            self.total_questions += 1
        
        input("\nPresiona Enter para continuar...")
    
    def combinatorics_game(self):
        """
        TEMA: COMBINATORIA
        
        Conceptos matemáticos:
        - Permutación: Ordenación de elementos donde el orden importa
        - P(n,r) = n! / (n-r)!
        - Combinación: Selección de elementos donde el orden NO importa
        - C(n,r) = n! / (r!(n-r)!)
        
        El jugador debe calcular permutaciones y combinaciones.
        """
        self.clear_screen()
        print("🎲 MÓDULO: COMBINATORIA")
        print("=" * 60)
        print("\n📚 CONCEPTOS:")
        print("• Permutación P(n,r): Ordenaciones de r elementos de n (orden importa)")
        print("  Fórmula: P(n,r) = n! / (n-r)!")
        print("\n• Combinación C(n,r): Selecciones de r elementos de n (orden NO importa)")
        print("  Fórmula: C(n,r) = n! / (r!(n-r)!)")
        print("\n" + "=" * 60)
        
        # Generar problema aleatorio
        problem_type = random.choice(["permutation", "combination"])
        
        if problem_type == "permutation":
            n = random.randint(5, 8)
            r = random.randint(2, min(4, n))
            
            print(f"\n❓ PROBLEMA DE PERMUTACIÓN:")
            print(f"¿De cuántas formas diferentes se pueden ordenar {r} libros")
            print(f"seleccionados de una colección de {n} libros?")
            print(f"\n(El orden de los libros importa)")
            
            # Calcular respuesta correcta: P(n,r) = n! / (n-r)!
            correct_answer = math.factorial(n) // math.factorial(n - r)
            formula = f"P({n},{r}) = {n}! / ({n}-{r})! = {n}! / {n-r}!"
            
        else:  # combination
            n = random.randint(5, 10)
            r = random.randint(2, min(5, n))
            
            print(f"\n❓ PROBLEMA DE COMBINACIÓN:")
            print(f"¿De cuántas formas se puede formar un comité de {r} personas")
            print(f"seleccionadas de un grupo de {n} personas?")
            print(f"\n(El orden NO importa)")
            
            # Calcular respuesta correcta: C(n,r) = n! / (r!(n-r)!)
            correct_answer = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
            formula = f"C({n},{r}) = {n}! / ({r}!×({n}-{r})!)"
        
        try:
            user_answer = int(input("\nTu respuesta (número entero): "))
            
            if user_answer == correct_answer:
                print("\n✅ ¡CORRECTO!")
                print(f"Fórmula aplicada: {formula}")
                print(f"Resultado: {correct_answer}")
                self.score += 10
                self.total_questions += 1
            else:
                print(f"\n❌ Incorrecto. La respuesta correcta es: {correct_answer}")
                print(f"Fórmula: {formula}")
                self.total_questions += 1
        except ValueError:
            print("\n❌ Entrada inválida. Debes ingresar un número entero.")
            self.total_questions += 1
        
        input("\nPresiona Enter para continuar...")
    
    def graph_theory_game(self):
        """
        TEMA: TEORÍA DE GRAFOS
        
        Conceptos matemáticos:
        - Grafo: Conjunto de vértices conectados por aristas
        - Camino más corto: Secuencia de aristas con peso mínimo
        - Algoritmo de Dijkstra (simplificado)
        
        El jugador debe encontrar el camino más corto entre dos nodos.
        """
        self.clear_screen()
        print("🗺️  MÓDULO: TEORÍA DE GRAFOS")
        print("=" * 60)
        print("\n📚 CONCEPTO:")
        print("Un grafo G = (V, E) consiste en vértices V y aristas E.")
        print("El camino más corto es la ruta con menor peso total entre dos nodos.")
        print("\n" + "=" * 60)
        
        # Crear un grafo simple representado como matriz de adyacencia
        # Grafo de ejemplo: A-B-C-D con pesos
        print("\n🗺️  GRAFO:")
        print("""
        A ---3--- B
        |         |
        5         2
        |         |
        C ---4--- D
        """)
        
        print("\nPesos de las aristas:")
        print("• A-B: 3")
        print("• A-C: 5")
        print("• B-D: 2")
        print("• C-D: 4")
        
        print("\n❓ ¿Cuál es el peso del camino más corto de A a D?")
        print("(Suma los pesos de las aristas en el camino más corto)")
        
        # Camino más corto: A -> B -> D = 3 + 2 = 5
        # Alternativa: A -> C -> D = 5 + 4 = 9
        correct_answer = 5
        correct_path = "A → B → D"
        
        try:
            user_answer = int(input("\nTu respuesta (peso total): "))
            
            if user_answer == correct_answer:
                print("\n✅ ¡CORRECTO!")
                print(f"El camino más corto es: {correct_path}")
                print(f"Peso total: 3 + 2 = {correct_answer}")
                print("\nOtro camino posible: A → C → D con peso 5 + 4 = 9")
                self.score += 10
                self.total_questions += 1
            else:
                print(f"\n❌ Incorrecto. El peso del camino más corto es: {correct_answer}")
                print(f"Camino: {correct_path}")
                print("Cálculo: 3 (A→B) + 2 (B→D) = 5")
                self.total_questions += 1
        except ValueError:
            print("\n❌ Entrada inválida. Debes ingresar un número entero.")
            self.total_questions += 1
        
        input("\nPresiona Enter para continuar...")
    
    def relations_game(self):
        """
        TEMA: RELACIONES
        
        Conceptos matemáticos:
        - Relación: Subconjunto del producto cartesiano A × B
        - Reflexiva: ∀a ∈ A, (a,a) ∈ R
        - Simétrica: Si (a,b) ∈ R entonces (b,a) ∈ R
        - Transitiva: Si (a,b) ∈ R y (b,c) ∈ R entonces (a,c) ∈ R
        
        El jugador debe identificar las propiedades de una relación dada.
        """
        self.clear_screen()
        print("🔗 MÓDULO: RELACIONES")
        print("=" * 60)
        print("\n📚 CONCEPTOS:")
        print("Una relación R sobre un conjunto A tiene estas propiedades:")
        print("\n• REFLEXIVA: Todo elemento se relaciona consigo mismo")
        print("  ∀a ∈ A, (a,a) ∈ R")
        print("\n• SIMÉTRICA: Si a se relaciona con b, entonces b se relaciona con a")
        print("  Si (a,b) ∈ R entonces (b,a) ∈ R")
        print("\n• TRANSITIVA: Si a→b y b→c, entonces a→c")
        print("  Si (a,b) ∈ R y (b,c) ∈ R entonces (a,c) ∈ R")
        print("\n" + "=" * 60)
        
        # Generar una relación de ejemplo
        relations = [
            {
                "name": "R₁",
                "set": "{1, 2, 3}",
                "pairs": [(1,1), (2,2), (3,3), (1,2), (2,1)],
                "reflexive": True,
                "symmetric": True,
                "transitive": True,
                "explanation": "Es reflexiva (todos los pares (a,a) están), simétrica (1,2 y 2,1 están), y transitiva (se cumple la propiedad)."
            },
            {
                "name": "R₂",
                "set": "{1, 2, 3}",
                "pairs": [(1,2), (2,3), (1,3)],
                "reflexive": False,
                "symmetric": False,
                "transitive": True,
                "explanation": "NO es reflexiva (faltan (1,1), (2,2), (3,3)), NO es simétrica (falta (2,1), (3,2), (3,1)), pero SÍ es transitiva."
            },
            {
                "name": "R₃",
                "set": "{1, 2, 3, 4}",
                "pairs": [(1,1), (2,2), (3,3), (4,4), (1,2), (2,1), (2,3), (3,2)],
                "reflexive": True,
                "symmetric": True,
                "transitive": False,
                "explanation": "Es reflexiva y simétrica, pero NO es transitiva porque (1,2) y (2,3) están en R, pero (1,3) no está."
            }
        ]
        
        relation = random.choice(relations)
        
        print(f"\n🔗 RELACIÓN: {relation['name']} sobre el conjunto A = {relation['set']}")
        print(f"\nPares ordenados en R: {relation['pairs']}")
        
        print("\n❓ ¿Qué propiedades tiene esta relación?")
        print("\n1. ¿Es REFLEXIVA? (s/n)")
        reflexive_answer = input("Tu respuesta: ").lower().strip()
        
        print("\n2. ¿Es SIMÉTRICA? (s/n)")
        symmetric_answer = input("Tu respuesta: ").lower().strip()
        
        print("\n3. ¿Es TRANSITIVA? (s/n)")
        transitive_answer = input("Tu respuesta: ").lower().strip()
        
        # Evaluar respuestas
        correct = 0
        total = 3
        
        if (reflexive_answer == 's' and relation['reflexive']) or (reflexive_answer == 'n' and not relation['reflexive']):
            correct += 1
            print("\n✅ Reflexiva: CORRECTO")
        else:
            print(f"\n❌ Reflexiva: INCORRECTO (es {'reflexiva' if relation['reflexive'] else 'NO reflexiva'})")
        
        if (symmetric_answer == 's' and relation['symmetric']) or (symmetric_answer == 'n' and not relation['symmetric']):
            correct += 1
            print("✅ Simétrica: CORRECTO")
        else:
            print(f"❌ Simétrica: INCORRECTO (es {'simétrica' if relation['symmetric'] else 'NO simétrica'})")
        
        if (transitive_answer == 's' and relation['transitive']) or (transitive_answer == 'n' and not relation['transitive']):
            correct += 1
            print("✅ Transitiva: CORRECTO")
        else:
            print(f"❌ Transitiva: INCORRECTO (es {'transitiva' if relation['transitive'] else 'NO transitiva'})")
        
        print(f"\n📊 Resultado: {correct}/{total} propiedades correctas")
        print(f"\n💡 Explicación: {relation['explanation']}")
        
        # Asignar puntos proporcionales
        self.score += (correct * 10) // total * 10
        self.total_questions += 1
        
        input("\nPresiona Enter para continuar...")
    
    def show_final_score(self):
        """Muestra la puntuación final del jugador"""
        self.clear_screen()
        print("📊 PUNTUACIÓN FINAL")
        print("=" * 60)
        print(f"\n🎯 Preguntas respondidas: {self.total_questions}")
        print(f"⭐ Puntuación total: {self.score} puntos")
        
        if self.total_questions > 0:
            percentage = (self.score / (self.total_questions * 10)) * 100
            print(f"📈 Porcentaje de aciertos: {percentage:.1f}%")
            
            if percentage >= 90:
                print("\n🏆 ¡EXCELENTE! Dominas los conceptos de Matemáticas Discretas.")
            elif percentage >= 70:
                print("\n👍 ¡MUY BIEN! Tienes un buen entendimiento de los temas.")
            elif percentage >= 50:
                print("\n📚 BIEN. Sigue practicando para mejorar tu comprensión.")
            else:
                print("\n💪 Sigue estudiando. Revisa los conceptos y vuelve a intentarlo.")
        
        print("\n" + "=" * 60)
        print("\n¡Gracias por jugar! 🎓")
        print("Recuerda: La práctica hace al maestro en Matemáticas Discretas.")
        print("\n" + "=" * 60)
    
    def run(self):
        """Ejecuta el juego principal"""
        print("\n🎮 Bienvenido al Juego Educativo de Matemáticas Discretas")
        print("Curso: MATH-112 - Nivel Universitario\n")
        input("Presiona Enter para comenzar...")
        
        while True:
            self.show_menu()
            choice = input("\nElige una opción (1-5): ").strip()
            
            if choice == "1":
                self.modular_arithmetic_game()
            elif choice == "2":
                self.combinatorics_game()
            elif choice == "3":
                self.graph_theory_game()
            elif choice == "4":
                self.relations_game()
            elif choice == "5":
                self.show_final_score()
                break
            else:
                print("\n❌ Opción inválida. Por favor elige 1-5.")
                input("Presiona Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    game = DiscreteMatGame()
    game.run()
