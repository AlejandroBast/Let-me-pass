import type { Module } from "@/app/page"

export interface Question {
  title: string
  question: string
  answer: string
  type: "text" | "multiple-choice"
  options?: string[]
  hint?: string
  explanation: string
  topic: string
}

// Cryptography questions - Modular arithmetic and Caesar cipher
function generateCryptoQuestion(): Question {
  const shift = Math.floor(Math.random() * 25) + 1
  const messages = [
    { plain: "HOLA", encrypted: caesarEncrypt("HOLA", shift) },
    { plain: "MATE", encrypted: caesarEncrypt("MATE", shift) },
    { plain: "EXITO", encrypted: caesarEncrypt("EXITO", shift) },
  ]
  const selected = messages[Math.floor(Math.random() * messages.length)]

  return {
    title: "🔐 Criptografía - Cifrado César",
    question: `Descifra el mensaje "${selected.encrypted}" que fue cifrado con un desplazamiento de ${shift} posiciones.`,
    answer: selected.plain,
    type: "text",
    hint: `Usa aritmética modular: (letra - ${shift}) mod 26`,
    explanation: `El cifrado César usa aritmética modular. Con desplazamiento ${shift}, cada letra se mueve ${shift} posiciones. Para descifrar, restamos ${shift} módulo 26. La respuesta es "${selected.plain}".`,
    topic: "Aritmética Modular",
  }
}

// Combinatorics questions
function generateCombinatoricsQuestion(): Question {
  const type = Math.random() > 0.5 ? "permutation" : "combination"

  if (type === "permutation") {
    const n = Math.floor(Math.random() * 4) + 5 // 5-8
    const r = Math.floor(Math.random() * 3) + 2 // 2-4
    const answer = permutation(n, r)

    return {
      title: "🎲 Combinatoria - Permutaciones",
      question: `¿De cuántas formas diferentes se pueden ordenar ${r} elementos de un conjunto de ${n} elementos? (Orden importa)`,
      answer: answer.toString(),
      type: "text",
      hint: `Usa la fórmula P(n,r) = n!/(n-r)!`,
      explanation: `Permutación P(${n},${r}) = ${n}!/(${n}-${r})! = ${answer}. El orden importa, por lo que cada arreglo diferente cuenta como una permutación distinta.`,
      topic: "Permutaciones",
    }
  } else {
    const n = Math.floor(Math.random() * 4) + 6 // 6-9
    const r = Math.floor(Math.random() * 3) + 2 // 2-4
    const answer = combination(n, r)

    return {
      title: "🎲 Combinatoria - Combinaciones",
      question: `¿De cuántas formas se pueden elegir ${r} elementos de un conjunto de ${n} elementos? (Orden NO importa)`,
      answer: answer.toString(),
      type: "text",
      hint: `Usa la fórmula C(n,r) = n!/(r!(n-r)!)`,
      explanation: `Combinación C(${n},${r}) = ${n}!/(${r}!×${n - r}!) = ${answer}. El orden no importa, solo importa qué elementos se seleccionan.`,
      topic: "Combinaciones",
    }
  }
}

// Graph theory questions
function generateGraphQuestion(): Question {
  const graphs = [
    {
      description: "un grafo con 4 vértices donde A→B(2), A→C(4), B→C(1), B→D(7), C→D(3)",
      question: "¿Cuál es la distancia del camino más corto de A a D?",
      answer: "6",
      path: "A→B→C→D",
      explanation:
        "El camino más corto es A→B(2) + B→C(1) + C→D(3) = 6. Usamos el algoritmo de Dijkstra para encontrar el camino de costo mínimo.",
    },
    {
      description: "un grafo con 5 vértices donde A→B(1), A→C(4), B→D(2), C→D(1), D→E(3)",
      question: "¿Cuál es la distancia del camino más corto de A a E?",
      answer: "6",
      path: "A→B→D→E",
      explanation:
        "El camino más corto es A→B(1) + B→D(2) + D→E(3) = 6. Este es un problema clásico de camino más corto en grafos ponderados.",
    },
  ]

  const selected = graphs[Math.floor(Math.random() * graphs.length)]

  return {
    title: "🗺️ Teoría de Grafos - Camino Más Corto",
    question: `En ${selected.description}, ${selected.question}`,
    answer: selected.answer,
    type: "text",
    hint: "Suma los pesos de las aristas en diferentes caminos y elige el menor",
    explanation: selected.explanation,
    topic: "Algoritmo de Dijkstra",
  }
}

// Relations questions
function generateRelationsQuestion(): Question {
  const relations = [
    {
      relation: "R = {(1,1), (2,2), (3,3), (1,2), (2,1)}",
      properties: ["Reflexiva", "Simétrica"],
      correct: "Reflexiva y Simétrica",
      explanation:
        "Es reflexiva porque cada elemento se relaciona consigo mismo. Es simétrica porque si (a,b) está en R, entonces (b,a) también está. No es transitiva porque (1,2) y (2,1) están pero no implican nada más.",
    },
    {
      relation: "R = {(1,1), (2,2), (1,2), (2,3), (1,3)}",
      properties: ["Reflexiva", "Transitiva"],
      correct: "Transitiva",
      explanation:
        "Es transitiva porque (1,2) y (2,3) implican (1,3), que está en R. No es reflexiva porque falta (3,3). No es simétrica porque (1,2) está pero (2,1) no.",
    },
    {
      relation: "R = {(1,2), (2,1), (2,3), (3,2)}",
      properties: ["Simétrica"],
      correct: "Simétrica",
      explanation:
        "Es simétrica porque para cada (a,b) en R, (b,a) también está en R. No es reflexiva porque ningún elemento se relaciona consigo mismo. No es transitiva porque (1,2) y (2,3) no implican (1,3).",
    },
  ]

  const selected = relations[Math.floor(Math.random() * relations.length)]
  const options = ["Reflexiva", "Simétrica", "Transitiva", "Reflexiva y Simétrica", "Simétrica y Transitiva", "Ninguna"]

  return {
    title: "🔗 Relaciones - Propiedades",
    question: `Dada la relación ${selected.relation} sobre el conjunto {1,2,3}, ¿qué propiedad(es) cumple?`,
    answer: selected.correct,
    type: "multiple-choice",
    options: options,
    hint: "Reflexiva: (a,a) para todo a. Simétrica: si (a,b) entonces (b,a). Transitiva: si (a,b) y (b,c) entonces (a,c)",
    explanation: selected.explanation,
    topic: "Propiedades de Relaciones",
  }
}

// Helper functions
function caesarEncrypt(text: string, shift: number): string {
  return text
    .split("")
    .map((char) => {
      const code = char.charCodeAt(0)
      if (code >= 65 && code <= 90) {
        return String.fromCharCode(((code - 65 + shift) % 26) + 65)
      }
      return char
    })
    .join("")
}

function factorial(n: number): number {
  if (n <= 1) return 1
  return n * factorial(n - 1)
}

function permutation(n: number, r: number): number {
  return factorial(n) / factorial(n - r)
}

function combination(n: number, r: number): number {
  return factorial(n) / (factorial(r) * factorial(n - r))
}

// Main question generator
export function generateQuestion(module: Module): Question {
  switch (module) {
    case "crypto":
      return generateCryptoQuestion()
    case "combinatorics":
      return generateCombinatoricsQuestion()
    case "graphs":
      return generateGraphQuestion()
    case "relations":
      return generateRelationsQuestion()
    default:
      return generateCryptoQuestion()
  }
}

export function checkAnswer(question: Question, userAnswer: string): boolean {
  const normalizedAnswer = userAnswer.trim().toUpperCase()
  const normalizedCorrect = question.answer.trim().toUpperCase()
  return normalizedAnswer === normalizedCorrect
}
