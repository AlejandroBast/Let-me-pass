"use client"

interface GameCompleteProps {
  score: number
  total: number
  onBackToMenu: () => void
}

export function GameComplete({ score, total, onBackToMenu }: GameCompleteProps) {
  const percentage = (score / total) * 100
  const isPerfect = score === total
  const isGood = percentage >= 70
  const isFair = percentage >= 50

  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-2xl mx-auto text-center">
        <div className="mb-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
          <div className="text-8xl mb-6 animate-float">{isPerfect ? "🏆" : isGood ? "🎉" : isFair ? "👍" : "💪"}</div>
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
            {isPerfect ? "¡Perfecto!" : isGood ? "¡Excelente!" : isFair ? "¡Buen trabajo!" : "¡Sigue practicando!"}
          </h1>
          <p className="text-xl text-muted-foreground">Has terminado el desafío</p>
        </div>

        <div
          className="p-8 mb-8 border-2 border-primary/50 animate-in fade-in slide-in-from-bottom-4 duration-700"
          style={{ animationDelay: "200ms" }}
        >
          <div className="mb-6">
            <p className="text-4xl font-bold text-primary">{score}/{total}</p>
            <p className="text-lg text-muted-foreground">Respuestas correctas</p>
          </div>

          <div className="w-full bg-muted rounded-full h-4 mb-4 overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-primary to-secondary transition-all duration-1000 animate-in slide-in-from-left"
              style={{ width: `${percentage}%` }}
            />
          </div>

          <p className="text-2xl font-bold text-primary">{Math.round(percentage)}%</p>
        </div>

        <div
          className="space-y-4 animate-in fade-in slide-in-from-bottom-4 duration-700"
          style={{ animationDelay: "400ms" }}
        >
          <button
            onClick={onBackToMenu}
            className="w-full px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary/90 transition"
          >
            Volver al menú
          </button>

          {!isPerfect && (
            <p className="text-sm text-muted-foreground">
              💡 Intenta de nuevo para mejorar tu puntuación
            </p>
          )}
        </div>

        {isPerfect && (
          <div className="mt-8 p-6 bg-gradient-to-r from-primary/20 to-secondary/20 rounded-lg border-2 border-primary animate-pulse-glow">
            <p className="text-lg font-medium">¡Has alcanzado la puntuación perfecta! 🌟</p>
          </div>
        )}
      </div>
    </div>
  )
}