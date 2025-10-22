"use client"

import { useEffect, useState } from "react"

interface BridgeSceneProps {
  progress: number
  feedback: "correct" | "incorrect" | null
}

export function BridgeScene({ progress, feedback }: BridgeSceneProps) {
  const [characterPosition, setCharacterPosition] = useState(0)
  const [showParticles, setShowParticles] = useState(false)
  // Añadimos estado local para el progreso del puente
  const [bridgeProgress, setBridgeProgress] = useState(progress)

  useEffect(() => {
    if (feedback === "correct") {
      setCharacterPosition(progress)
      setBridgeProgress(progress)
      setShowParticles(true)
      setTimeout(() => setShowParticles(false), 1000)
    } else if (feedback === "incorrect") {
      // Reducimos el progreso del puente en 20% (2 piezas)
      const newProgress = Math.max(0, bridgeProgress - 20)
      setBridgeProgress(newProgress)
      setCharacterPosition(newProgress)
    }
  }, [feedback, progress])

  const bridgePieces = 10
  // Usamos bridgeProgress en lugar de progress para las piezas completadas
  const completedPieces = Math.floor((bridgeProgress / 100) * bridgePieces)


  return (
    <div className="relative w-full h-64 mb-8 bg-gradient-to-b from-card to-muted rounded-xl overflow-hidden border-2 border-border">
      {/* Fondo del cielo */}
      <div className="absolute inset-0 bg-gradient-to-b from-blue-900/20 to-transparent" />

  {/* Montañas/acantilados */}
      <div className="absolute bottom-0 left-0 w-1/4 h-32 bg-gradient-to-t from-muted to-muted/50 rounded-tr-3xl" />
      <div className="absolute bottom-0 right-0 w-1/4 h-32 bg-gradient-to-t from-muted to-muted/50 rounded-tl-3xl" />

  {/* Puente */}
      <div className="absolute bottom-16 left-1/4 right-1/4 h-4 flex gap-1">
        {Array.from({ length: bridgePieces }).map((_, i) => (
          <div
            key={i}
            className={`flex-1 transition-all duration-500 ${
              i < completedPieces
                ? "bg-gradient-to-r from-primary to-secondary opacity-100 animate-in slide-in-from-bottom-4"
                : "bg-border/30 opacity-50"
            }`}
            style={{
              animationDelay: `${i * 50}ms`,
              boxShadow: i < completedPieces ? "0 4px 20px rgba(0, 217, 255, 0.4)" : "none",
            }}
          />
        ))}
      </div>

  {/* Soportes del puente */}
      {Array.from({ length: bridgePieces + 1 }).map((_, i) => {
        const isVisible = i <= completedPieces
        return (
          <div
            key={`support-${i}`}
            className={`absolute bottom-0 w-1 h-16 bg-primary/50 transition-all duration-500 ${
              isVisible ? "opacity-100" : "opacity-0"
            }`}
            style={{
              left: `calc(25% + ${(i / bridgePieces) * 50}%)`,
            }}
          />
        )
      })}

  {/* Personaje */}
      <div
        className="absolute bottom-20 w-12 h-12 transition-all duration-1000 ease-out"
        style={{
          left: `calc(25% + ${(characterPosition / 100) * 50}% - 24px)`,
        }}
      >
        <div className="relative animate-float">
          <div className="text-4xl">🏃🏻‍➡️</div>
          {showParticles && (
            <div className="absolute inset-0">
              {Array.from({ length: 8 }).map((_, i) => (
                <div
                  key={i}
                  className="absolute w-2 h-2 bg-primary rounded-full animate-ping"
                  style={{
                    left: `${Math.random() * 100}%`,
                    top: `${Math.random() * 100}%`,
                    animationDelay: `${i * 100}ms`,
                  }}
                />
              ))}
            </div>
          )}
        </div>
      </div>

  {/* Bandera meta */}
      <div className="absolute bottom-20 right-[23%] text-4xl animate-float">🏁</div>

  {/* Capa de retroalimentación */}
      {feedback === "correct" && <div className="absolute inset-0 bg-success/10 animate-in fade-in duration-300" />}
      {feedback === "incorrect" && (
        <div className="absolute inset-0 bg-destructive/10 animate-in fade-in duration-300" />
      )}
    </div>
  )
}
