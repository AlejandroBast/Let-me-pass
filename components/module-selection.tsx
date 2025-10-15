"use client"

import type { Module } from "@/lib/questions"

interface ModuleSelectionProps {
  onSelectModule: (module: Module) => void
}

const modules = [
  {
    id: "crypto" as Module,
    title: "Criptografía",
    description: "Descifra mensajes usando aritmética modular",
    icon: "🔐",
    color: "from-cyan-500 to-blue-500",
  },
  {
    id: "combinatorics" as Module,
    title: "Combinatoria",
    description: "Resuelve permutaciones y combinaciones",
    icon: "🎲",
    color: "from-purple-500 to-pink-500",
  },
  {
    id: "graphs" as Module,
    title: "Teoría de Grafos",
    description: "Encuentra el camino más corto",
    icon: "🗺️",
    color: "from-green-500 to-emerald-500",
  },
  {
    id: "relations" as Module,
    title: "Relaciones",
    description: "Identifica propiedades de relaciones",
    icon: "🔗",
    color: "from-orange-500 to-red-500",
  },
]

export function ModuleSelection({ onSelectModule }: ModuleSelectionProps) {
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-12 animate-in fade-in slide-in-from-bottom-4 duration-700">
        <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
          Let me pass
        </h1>
        <p className="text-xl text-muted-foreground max-w-2xl mx-auto text-balance">
          Ayuda al personaje a cruzar el puente resolviendo problemas de matemáticas discretas.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {modules.map((module, index) => (
          <div
            key={module.id}
            className="group relative overflow-hidden border-2 border-border hover:border-primary transition-all duration-300 hover:scale-105 hover:shadow-2xl hover:shadow-primary/20 cursor-pointer animate-in fade-in slide-in-from-bottom-4"
            style={{ animationDelay: `${index * 100}ms` }}
            onClick={() => onSelectModule(module.id)}
          >
            <div
              className={`absolute inset-0 bg-gradient-to-br ${module.color} opacity-0 group-hover:opacity-10 transition-opacity duration-300`}
            />

            <div className="p-6 relative z-10">
              <div className="text-6xl mb-4 animate-float">{module.icon}</div>
              <h3 className="text-2xl font-bold mb-2 group-hover:text-primary transition-colors">{module.title}</h3>
              <p className="text-muted-foreground mb-4">{module.description}</p>
              <button
                className="mt-4 px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary/90 transition"
                onClick={() => onSelectModule(module.id)}
              >
                Comenzar
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="mt-12 text-center">
        <div className="inline-block p-6 border-primary/50">
          <p className="text-sm text-muted-foreground">
            <span className="font-bold text-primary">MATH-112</span> - Universidad de Matemáticas Discretas
          </p>
        </div>
      </div>
    </div>
  )
}
