# 🎓 Guía del Juego Educativo de Matemáticas Discretas

## 📋 Descripción General

Este es un juego educativo interactivo diseñado para estudiantes del curso MATH-112 (Matemáticas Discretas, nivel universitario). El juego cubre cuatro temas fundamentales del curso y proporciona retroalimentación inmediata para reforzar el aprendizaje.

## 🎯 Propósito Didáctico

### Objetivos de Aprendizaje:

1. **Aritmética Modular y Criptografía**
   - Comprender el concepto de congruencia modular
   - Aplicar aritmética modular en cifrado César
   - Entender la fórmula: C = (P + k) mod n

2. **Combinatoria**
   - Diferenciar entre permutaciones y combinaciones
   - Aplicar las fórmulas: P(n,r) = n!/(n-r)! y C(n,r) = n!/(r!(n-r)!)
   - Resolver problemas prácticos de conteo

3. **Teoría de Grafos**
   - Comprender la estructura de un grafo (vértices y aristas)
   - Encontrar caminos más cortos entre nodos
   - Aplicar conceptos básicos del algoritmo de Dijkstra

4. **Relaciones**
   - Identificar propiedades de relaciones: reflexiva, simétrica, transitiva
   - Analizar pares ordenados en una relación
   - Aplicar definiciones formales de propiedades

## 🚀 Cómo Jugar

### Requisitos:
- Python 3.6 o superior
- No requiere conexión a internet
- No requiere bibliotecas externas (solo módulos estándar de Python)

### Instrucciones de Ejecución:

1. **Ejecutar el juego:**
   \`\`\`bash
   python scripts/discrete_math_game.py
   \`\`\`

2. **Navegación:**
   - El juego presenta un menú con 5 opciones
   - Selecciona un número (1-4) para jugar un módulo específico
   - Selecciona 5 para ver tu puntuación final y salir

3. **Jugando cada módulo:**
   - Lee cuidadosamente la explicación del concepto matemático
   - Analiza el problema presentado
   - Ingresa tu respuesta cuando se te solicite
   - Recibe retroalimentación inmediata
   - Aprende de las explicaciones detalladas

4. **Sistema de Puntuación:**
   - Cada respuesta correcta otorga 10 puntos
   - El módulo de Relaciones otorga puntos proporcionales (por cada propiedad correcta)
   - Al final, verás tu puntuación total y porcentaje de aciertos

## 📚 Conceptos Matemáticos Aplicados

### 1. Aritmética Modular (Cifrado César)
**Concepto:** La aritmética modular trabaja con residuos de divisiones. En el cifrado César, cada letra se desplaza k posiciones en el alfabeto.

**Fórmulas:**
- Cifrado: C = (P + k) mod 26
- Descifrado: P = (C - k) mod 26

**Aplicación:** Criptografía básica, seguridad de información

### 2. Combinatoria
**Conceptos:**
- **Permutación:** Ordenación de elementos donde el orden importa
  - Fórmula: P(n,r) = n! / (n-r)!
  - Ejemplo: Ordenar 3 libros de 5 disponibles

- **Combinación:** Selección de elementos donde el orden NO importa
  - Fórmula: C(n,r) = n! / (r!(n-r)!)
  - Ejemplo: Elegir 3 personas de un grupo de 5

**Aplicación:** Probabilidad, análisis de algoritmos, teoría de juegos

### 3. Teoría de Grafos
**Conceptos:**
- Grafo G = (V, E): Conjunto de vértices V y aristas E
- Camino: Secuencia de vértices conectados por aristas
- Peso: Valor asociado a cada arista
- Camino más corto: Ruta con peso mínimo total

**Aplicación:** Redes de computadoras, GPS, optimización de rutas

### 4. Relaciones
**Conceptos:**
- **Reflexiva:** ∀a ∈ A, (a,a) ∈ R
  - Todo elemento se relaciona consigo mismo
  
- **Simétrica:** Si (a,b) ∈ R entonces (b,a) ∈ R
  - La relación es bidireccional
  
- **Transitiva:** Si (a,b) ∈ R y (b,c) ∈ R entonces (a,c) ∈ R
  - La relación se propaga

**Aplicación:** Bases de datos, lógica, teoría de conjuntos

## 💡 Consejos para Estudiantes

1. **Lee las explicaciones:** Cada módulo comienza con una explicación del concepto. Léela cuidadosamente.

2. **Practica múltiples veces:** Cada vez que juegas, se generan problemas aleatorios diferentes.

3. **Aprende de los errores:** Cuando fallas, lee la explicación detallada para entender tu error.

4. **Usa papel y lápiz:** Para problemas de combinatoria y grafos, es útil hacer cálculos en papel.

5. **Repasa las fórmulas:** Antes de jugar, repasa las fórmulas clave de cada tema.

## 🎓 Evaluación del Aprendizaje

El juego evalúa tu comprensión mediante:
- Problemas de aplicación directa de fórmulas
- Análisis de estructuras matemáticas
- Identificación de propiedades
- Resolución de problemas prácticos

**Interpretación de resultados:**
- 90-100%: Excelente dominio de los conceptos
- 70-89%: Buen entendimiento, sigue practicando
- 50-69%: Comprensión básica, necesitas más estudio
- <50%: Revisa los conceptos fundamentales

## 🔧 Características Técnicas

- **Lenguaje:** Python 3
- **Dependencias:** Solo bibliotecas estándar (random, math, typing)
- **Ejecución:** Local, sin necesidad de internet
- **Interfaz:** Consola/terminal
- **Portabilidad:** Funciona en Windows, macOS y Linux

## 📖 Referencias Académicas

Este juego está basado en conceptos estándar de Matemáticas Discretas cubiertos en cursos universitarios de primer año de Ciencias de la Computación e Ingeniería.

**Temas del curso MATH-112:**
- ✅ Conjuntos (implícito en relaciones)
- ✅ Relaciones (módulo dedicado)
- ✅ Funciones (implícito en grafos)
- ✅ Combinatoria (módulo dedicado)
- ✅ Aritmética modular (módulo dedicado)
- ✅ Grafos (módulo dedicado)

---

**¡Disfruta aprendiendo Matemáticas Discretas de forma interactiva! 🎮📚**
