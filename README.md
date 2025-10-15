# Let me pass

Let me pass es una aplicación educativa interactiva para practicar conceptos de Matemáticas Discretas a través de minijuegos. El jugador ayuda a un personaje a cruzar un puente resolviendo preguntas sobre cuatro módulos: Criptografía, Combinatoria, Teoría de Grafos y Relaciones.

Contenido del repositorio
- `app/` – aplicación Next.js (páginas, layout y estilos).
- `components/` – componentes React reutilizables (escena del puente, pantalla de juego, selección de módulo, resultados, etc.).
- `lib/` – generación de preguntas y utilidades (aquí está la lógica de los minijuegos).
- `public/` – recursos estáticos.
- `GUIA_JUEGO.md` – guía del juego.

Requisitos
- Node.js >= 18
- pnpm (recomendado) o npm/yarn

Instalación (con pnpm)
```bash
pnpm install
pnpm dev
```

Si usas npm:
```bash
npm install
npm run dev
```

Estructura de los minijuegos

1) Criptografía (crypto)
- Tipo: texto.
- Dinámica: el generador crea un mensaje en mayúsculas cifrado con un desplazamiento tipo César. El jugador debe descifrar y escribir el texto plano (sin acentos). 
- Ejemplo de uso: si la pregunta muestra `KRDQ` con desplazamiento 3, la respuesta esperada es `HOLA`.
- Sugerencia: el validador normaliza entradas (quita acentos y espacios, compara en minúsculas) para mayor tolerancia a la entrada.

2) Combinatoria (combinatorics)
- Tipo: texto.
- Dinámica: alterna entre permutaciones y combinaciones con parámetros aleatorios. La respuesta es un número (entero) con el resultado de la fórmula correspondiente.
- Fórmulas usadas:
  - Permutación P(n,r) = n! / (n-r)!
  - Combinación C(n,r) = n! / (r!(n-r)!)

3) Teoría de Grafos (graphs)
- Tipo: texto.
- Dinámica: problemas de camino más corto con grafos pequeños y pesos. El generador elige casos predefinidos y presenta la distancia mínima esperada como respuesta.

4) Relaciones (relations)
- Tipo: multiple-choice.
- Dinámica: presenta una relación en un conjunto (por ejemplo {(1,1),(1,2),(2,1)}) y el jugador selecciona qué propiedades cumple (Reflexiva, Simétrica, Transitiva, combinaciones, Ninguna). El generador normaliza opciones y la UI permite seleccionar una opción y enviarla.

Notas técnicas
- El tipo `Module` y la lógica de generación/validación de preguntas están en `lib/questions.ts`.
- `checkAnswer` normaliza las respuestas con NFD y remueve marcas diacríticas para comparar sin sensibilidad a acentos.
- El número de preguntas por sesión está fijado en 5 (archivo `components/game-play.tsx`) — puede parametrizarse fácilmente.

Buenas prácticas para desarrollo
- Ejecuta `pnpm dev` y abre `http://localhost:3000`.
- Si cambias `lib/questions.ts`, añade tests unitarios para `generateQuestion` y `checkAnswer`.

Cómo contribuir
- Hacer fork/branch. Crear PR con descripciones claras.
- Añadir tests para cambios en la generación o validación de preguntas.

Archivos eliminados / limpieza
- He eliminado los artefactos de build (`.next/`) y el lockfile duplicado `package-lock.json` (el proyecto usa pnpm y contiene `pnpm-lock.yaml`).

Restauración rápida (si necesitas revertir eliminaciones)
- Si borraste `.next/` por error, simplemente reconstruye:
```bash
pnpm build
pnpm dev
```

Más adelante puedo:
- Añadir tests unitarios (vitest / jest) para `lib/questions.ts`.
- Añadir i18n para inglés/español.
- Parametrizar número de preguntas y tiempo de transición.

Si quieres, puedo añadir ahora los tests unitarios y/o configurar CI básico para ejecutar tests en PRs.

---
© Proyecto Let me pass
# 🎓 Juego Educativo de Matemáticas Discretas

Un juego interactivo en Python diseñado para enseñar y evaluar conceptos de Matemáticas Discretas a nivel universitario (MATH-112).

## 🎯 Características

- **4 módulos educativos** cubriendo temas clave de Matemáticas Discretas
- **Retroalimentación inmediata** con explicaciones detalladas
- **Problemas aleatorios** para práctica ilimitada
- **Sistema de puntuación** para seguir tu progreso
- **Sin dependencias externas** - solo Python estándar
- **Funciona offline** - no requiere conexión a internet

## 📚 Temas Cubiertos

1. **🔐 Aritmética Modular y Criptografía** - Cifrado César
2. **🎲 Combinatoria** - Permutaciones y Combinaciones
3. **🗺️ Teoría de Grafos** - Caminos más cortos
4. **🔗 Relaciones** - Propiedades (reflexiva, simétrica, transitiva)

## 🚀 Cómo Ejecutar

\`\`\`bash
python scripts/discrete_math_game.py
\`\`\`

## 📖 Documentación

Consulta `GUIA_JUEGO.md` para:
- Guía completa de cómo jugar
- Explicación detallada de conceptos matemáticos
- Propósito didáctico de cada módulo
- Consejos para estudiantes

## 🎮 Ejemplo de Uso

\`\`\`
🎓 JUEGO EDUCATIVO DE MATEMÁTICAS DISCRETAS 🎓
============================================================

Selecciona un módulo para jugar:

1. 🔐 Aritmética Modular y Criptografía
2. 🎲 Combinatoria (Permutaciones y Combinaciones)
3. 🗺️  Teoría de Grafos (Caminos más cortos)
4. 🔗 Relaciones (Propiedades)
5. 📊 Ver puntuación final y salir
\`\`\`

## 🎓 Propósito Educativo

Este juego está diseñado para:
- Reforzar conceptos teóricos con aplicaciones prácticas
- Proporcionar práctica interactiva
- Ofrecer retroalimentación inmediata
- Evaluar la comprensión de temas clave

## 📊 Sistema de Evaluación

- Cada respuesta correcta: **10 puntos**
- Puntuación final con porcentaje de aciertos
- Evaluación cualitativa del desempeño

---

**Desarrollado para el curso MATH-112 - Matemáticas Discretas**
