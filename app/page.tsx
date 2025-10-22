"use client"

import { useState } from "react"
import { ModuleSelection } from "@/components/module-selection"
import { GamePlay } from "@/components/game-play"
import { GameComplete } from "@/components/game-complete"

import type { Module } from "@/lib/questions"

export default function Home() {
  const [gameState, setGameState] = useState<"menu" | "playing" | "complete">("menu")
  const [selectedModule, setSelectedModule] = useState<Module | null>(null)
  const [score, setScore] = useState(0)
  const [totalQuestions, setTotalQuestions] = useState(0)

  const handleModuleSelect = (module: Module) => {
    setSelectedModule(module)
    setGameState("playing")
    setScore(0)
    setTotalQuestions(0)
  }

  const handleGameComplete = (finalScore: number, total: number) => {
    setScore(finalScore)
    setTotalQuestions(total)
    setGameState("complete")
  }

  const handleBackToMenu = () => {
    setGameState("menu")
    setSelectedModule(null)
  }

  return (
    <main className="min-h-screen bg-background relative overflow-hidden">
  {/* Patrón de fondo animado */}
      <div className="absolute inset-0 opacity-10">
        <div
          className="absolute inset-0"
          style={{
            backgroundImage: `
            linear-gradient(90deg, oklch(0.7 0.2 195 / 0.1) 1px, transparent 1px),
            linear-gradient(oklch(0.7 0.2 195 / 0.1) 1px, transparent 1px)
          `,
            backgroundSize: "50px 50px",
          }}
        />
      </div>

      <div className="relative z-10">
        {gameState === "menu" && <ModuleSelection onSelectModule={handleModuleSelect} />}

        {gameState === "playing" && selectedModule && (
          <GamePlay module={selectedModule} onComplete={handleGameComplete} onBackToMenu={handleBackToMenu} />
        )}

        {gameState === "complete" && (
          <GameComplete score={score} total={totalQuestions} onBackToMenu={handleBackToMenu} />
        )}
      </div>
    </main>
  )
}
