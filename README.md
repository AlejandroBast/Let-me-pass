# Let me pass

Let me pass es una aplicación educativa interactiva para practicar conceptos de Matemáticas Discretas a través de minijuegos. El jugador ayuda a un personaje a cruzar un puente resolviendo preguntas sobre cuatro módulos: Criptografía, Combinatoria, Teoría de Grafos y Relaciones.

Contenido del repositorio
- `app/` – aplicación Next.js (páginas, layout y estilos).
- `components/` – componentes React reutilizables (escena del puente, pantalla de juego, selección de módulo, resultados, etc.).
- `lib/` – generación de preguntas y utilidades (aquí está la lógica de los minijuegos).
- `public/` – recursos estáticos.
- `GUIA_JUEGO.md` – guía del juego.

# Let Me Pass

Let Me Pass es una aplicación web interactiva para practicar conceptos de Matemáticas Discretas mediante minijuegos. El jugador ayuda a un personaje a cruzar un puente respondiendo preguntas sobre cuatro módulos: Criptografía (Cifrado César), Combinatoria, Teoría de Grafos y Relaciones.

## Estructura del repositorio (resumen)
- `app/` – aplicación Next.js (páginas y layout).
- `components/` – componentes React (pantalla de juego, selección de módulo, escena del puente, resultados).
- `lib/` – lógica de generación de preguntas y validación (`lib/questions.ts`).
- `public/` – assets estáticos.
- `GUIA_JUEGO.md` – guía didáctica adicional.

## Requisitos
- Node.js >= 18
- pnpm (recomendado) o npm/yarn

## Instalación rápida
Con pnpm (recomendado):
```bash
pnpm install
pnpm dev
```

Con npm:
```bash
npm install
npm run dev
```

## Cómo se aplican los 4 temas en el proyecto (operaciones, fórmulas y código)

En las siguientes secciones encontrarás: (1) la idea matemática, (2) la operación/algoritmo usado, (3) dónde está implementado en el código y (4) ejemplos concretos.

### 🔐 1) Aritmética Modular y Criptografía — Cifrado César

- Idea matemática
  - El cifrado César desplaza cada letra del alfabeto un número fijo de posiciones. Esta operación es un ejemplo sencillo de aritmética modular sobre 26 letras.

- Operación / fórmula
  - Para cifrar: C = (P + k) mod 26
    - P: índice de la letra en 0..25 (A=0, B=1, ...)
    - k: desplazamiento (1..25)
    - C: índice cifrado
  - Para descifrar: P = (C - k + 26) mod 26
- Ideas de ampliación
  - Modo oculto: no mostrar `k` (más difícil).
  - Incluir cifrado sobre caracteres adicionales o texto completo (no solo mayúsculas A-Z).

### 🎲 2) Combinatoria — Permutaciones y Combinaciones

- Idea matemática
  - Permutaciones: conteo de arreglos donde el orden importa.
  - Combinaciones: conteo de selecciones donde el orden no importa.

- Operaciones / fórmulas
  - Factorial: n! = n × (n-1) × ... × 1
  - Permutación P(n,r) = n! / (n - r)!
  - Combinación C(n,r) = n! / (r! (n - r)!)

- Implementación en el proyecto
  - Generador: `lib/questions.ts` → `generateCombinatoricsQuestion()` selecciona aleatoriamente tipo (permutación o combinación), valores de `n` y `r`, y calcula la respuesta con `permutation(n,r)` o `combination(n,r)`.
  - Helpers: `lib/questions.ts` → `factorial`, `permutation`, `combination`.
  - UI: `components/game-play.tsx` muestra la pregunta y acepta la respuesta numérica en el textarea.

- Ejemplo práctico
  - Si el generador hace n=6, r=3 y el tipo es permutación: P(6,3) = 6!/(6-3)! = 6×5×4 = 120.
  - Pregunta: "¿De cuántas formas diferentes se pueden ordenar 3 elementos de un conjunto de 6?" Respuesta esperada: `120`.

- Cómo valida el código
  - `checkAnswer` compara la entrada normalizada con el número esperado convertido a string.
  - Recomendación: mejorar `normalizeText` para aceptar formatos numéricos con separadores (`1.200` o `1 200`) si lo deseas.

- Ideas de ampliación
  - Mostrar la fórmula y un cálculo paso a paso en la explicación.
  - Aceptar respuestas en notación científica o con separadores.

### 🗺️ 3) Teoría de Grafos — Caminos más cortos

- Idea matemática
  - Encontrar el camino de coste mínimo entre dos nodos en un grafo ponderado.
  - Algoritmo clásico: Dijkstra para grafos con pesos no negativos.

- Operación / algoritmo
  - Dijkstra: construir tabla de distancias mínimas desde el origen y relajación de aristas.

- Implementación en el proyecto
  - Actualmente: `lib/questions.ts` → `generateGraphQuestion()` utiliza ejemplos predefinidos (pequeños grafos con pesos) y devuelve la distancia mínima conocida como respuesta.
  - Nota: no hay una implementación dinámica de Dijkstra actualmente (se usan casos fijos). El cálculo de la respuesta para cada caso está precalculado o documentado en la entrada.

- Ejemplo práctico
  - Grafo: A→B(2), A→C(4), B→C(1), B→D(7), C→D(3).
  - Camino más corto A→D = A→B(2) + B→C(1) + C→D(3) = 6.
  - Pregunta: "¿Cuál es la distancia del camino más corto de A a D?" Respuesta: `6`.

- Cómo valida el código
  - `checkAnswer` compara la entrada con la respuesta esperada (número).

- Ideas de ampliación
  - Implementar generador de grafos aleatorios y ejecutar Dijkstra en `lib/questions.ts` para calcular la respuesta automáticamente.
  - Añadir visualización interactiva del grafo (canvas / SVG / D3) que muestre el camino y los pesos.

### 🔗 4) Relaciones — Propiedades (Reflexiva, Simétrica, Transitiva)

- Idea matemática
  - Dada una relación R sobre un conjunto, comprobar si cumple propiedades:
    - Reflexiva: para todo a en el conjunto, (a,a) ∈ R.
    - Simétrica: si (a,b) ∈ R entonces (b,a) ∈ R.
    - Transitiva: si (a,b) ∈ R y (b,c) ∈ R entonces (a,c) ∈ R.

- Implementación en el proyecto
  - Generador: `lib/questions.ts` → `generateRelationsQuestion()` elige relaciones predefinidas y prepara la opción correcta entre un conjunto de opciones (Reflexiva, Simétrica, Transitiva, combinaciones, Ninguna).
  - UI: `components/game-play.tsx` presenta botones para elegir la respuesta (multiple-choice).

- Ejemplo práctico
  - R = {(1,1), (2,2), (3,3), (1,2), (2,1)} sobre {1,2,3} → Reflexiva y Simétrica.
  - Pregunta: "¿Qué propiedad(es) cumple R?" Opciones: Reflexiva, Simétrica, Transitiva, Reflexiva y Simétrica, ... → Respuesta: "Reflexiva y Simétrica".

- Cómo valida el código
  - La comparación usa `checkAnswer`, que compara la opción seleccionada (texto) con la respuesta esperada. Para mayor robustez se entrega la opción como texto exacto en `question.answer`.

- Ideas de ampliación
  - Generar relaciones aleatorias y comprobar las propiedades programáticamente en tiempo real (analizar pares en conjuntos y derivar reflexividad/simetría/transitividad).
  - Permitir respuestas multi-selección (marcar varias propiedades a la vez) en vez de una sola opción compuesta.

## Validación y normalización de respuestas
- Función central: `lib/questions.ts` → `checkAnswer(question, userAnswer)`.
- Normalización actual:
  - `trim()`, `toLowerCase()` y normalización Unicode NFD para eliminar acentos (se eliminan las marcas diacríticas con una expresión compatible).
  - Comparación exacta entre la respuesta normalizada y la solución normalizada.

## Dónde modificar / añadir lógica
- `lib/questions.ts` → punto central para generar preguntas y comprobar respuestas.
- `components/game-play.tsx` → controla el flujo del juego, interacciones de usuario, scoring y transición entre preguntas.
- `components/module-selection.tsx` → selección de módulo y textos descriptivos.

## Recomendaciones para pruebas y mejoras
- Escribe tests unitarios para `generateQuestion()` y `checkAnswer()` (usar vitest o jest). Casos sugeridos:
  - Criptografía: distintas mayúsculas/acentos, variaciones de `shift`.
  - Combinatoria: comprobaciones numéricas (factorial, overflow, límites).
  - Grafos: casos con respuestas predefinidas y (si se añade) Dijkstra.
  - Relaciones: varias relaciones que ejerciten cada propiedad.

## Próximos pasos sugeridos
- Implementar Dijkstra para grafos aleatorios en `lib/questions.ts`.
- Soporte multi-selección para el módulo de Relaciones.
- Añadir tests automáticos y CI.

## Contacto / Contribución
- Haz fork, crea una branch y abre PR con una descripción clara del cambio.
- Añade tests para cambios que afecten la generación o validación de preguntas.

---
© Proyecto Let me pass
