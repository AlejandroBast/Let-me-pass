"use client"

import { useState, useEffect } from "react"
import type { Module } from "@/lib/questions"
import { BridgeScene } from "@/components/bridge-scene"
import { generateQuestion, checkAnswer, type Question } from "@/lib/questions"

interface GamePlayProps {
  module: Module
  onComplete: (score: number, total: number) => void
  onBackToMenu: () => void
}

export function GamePlay({ module, onComplete, onBackToMenu }: GamePlayProps) {
  const [currentQuestion, setCurrentQuestion] = useState<Question | null>(null)
  const [userAnswer, setUserAnswer] = useState("")
  const [feedback, setFeedback] = useState<"correct" | "incorrect" | null>(null)
  const [score, setScore] = useState(0)
  const [questionNumber, setQuestionNumber] = useState(1)
  const [bridgeProgress, setBridgeProgress] = useState(0)
  const [isAnswering, setIsAnswering] = useState(false)
  const totalQuestions = 5

  useEffect(() => {
    setCurrentQuestion(generateQuestion(module))
  }, [module])

  const handleSubmit = () => {
    if (!currentQuestion || isAnswering) return

    // For multiple-choice ensure user selected an option
    if (currentQuestion.type === "multiple-choice" && !userAnswer) return

    setIsAnswering(true)
    const isCorrect = checkAnswer(currentQuestion, userAnswer)
    setFeedback(isCorrect ? "correct" : "incorrect")

    // update score and bridge immediately for UI
    const newScore = score + (isCorrect ? 1 : 0)
    setScore(newScore)
    const progress = (questionNumber / totalQuestions) * 100
    setBridgeProgress(progress)

    setTimeout(() => {
      if (questionNumber >= totalQuestions) {
        onComplete(newScore, totalQuestions)
      } else {
        setQuestionNumber((n) => n + 1)
        setCurrentQuestion(generateQuestion(module))
        setUserAnswer("")
        setFeedback(null)
        setIsAnswering(false)
      }
    }, 1200)
  }

  if (!currentQuestion) return null

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="flex justify-between items-center mb-6">
          <button
            onClick={onBackToMenu}
            className="px-4 py-2 bg-secondary text-white rounded-lg hover:bg-secondary/90 transition"
          >
            Volver al menú
          </button>
          <div className="text-right">
            <p className="text-sm text-muted-foreground">
              Pregunta {questionNumber} de {totalQuestions}
            </p>
            <p className="text-lg font-bold text-primary">
              Puntuación: {score}/{questionNumber - 1}
            </p>
          </div>
        </div>

        {/* Bridge Scene */}
        <BridgeScene progress={bridgeProgress} feedback={feedback} />

        {/* Progress Bar */}
        <div className="mb-6">
          <div className="w-full bg-muted rounded-full h-4 overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-primary to-secondary transition-all duration-1000"
              style={{ width: `${(questionNumber - 1) / totalQuestions * 100}%` }}
            />
          </div>
        </div>

        {/* Question Card */}
        <div className="p-8 border-2 border-border animate-in fade-in slide-in-from-bottom-4">
          <div className="mb-6">
            <h2 className="text-2xl font-bold mb-4 text-primary">{currentQuestion.title}</h2>
            <p className="text-lg mb-4 leading-relaxed">{currentQuestion.question}</p>

            {currentQuestion.hint && (
              <div className="bg-muted/50 p-4 rounded-lg mb-4">
                <p className="text-sm text-muted-foreground">
                  <span className="font-bold">💡 Pista:</span> {currentQuestion.hint}
                </p>
              </div>
            )}
          </div>

          {currentQuestion.type === "multiple-choice" ? (
            <div className="space-y-3">
              {currentQuestion.options?.map((option, index) => (
                <button
                  key={index}
                  onClick={() => setUserAnswer(option)}
                  className={`w-full text-left px-4 py-3 border border-border rounded-lg hover:bg-muted/50 transition ${
                    userAnswer === option ? "bg-primary/20 border-primary" : ""
                  }`}
                  disabled={isAnswering}
                >
                  {option}
                </button>
              ))}
            </div>
          ) : (
            <textarea
              value={userAnswer}
              onChange={(e) => setUserAnswer(e.target.value)}
              placeholder="Escribe tu respuesta aquí..."
              className="w-full p-4 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition disabled:opacity-50 disabled:cursor-not-allowed"
              rows={4}
              disabled={isAnswering}
            />  
          )}

          <button
            onClick={handleSubmit}
            className="mt-6 w-full px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary/90 transition disabled:opacity-50 disabled:cursor-not-allowed"
            disabled={!userAnswer.trim() || isAnswering}
          >
            {isAnswering ? "Procesando..." : "Enviar Respuesta"}
          </button>

          {feedback && (
            <div
              className={`mt-6 p-6 rounded-lg animate-in fade-in slide-in-from-bottom-2 ${
                feedback === "correct"
                  ? "bg-success/20 border-2 border-success"
                  : "bg-destructive/20 border-2 border-destructive"
              }`}
            >
              <p className="font-bold text-lg mb-2">{feedback === "correct" ? "✅ ¡Correcto!" : "❌ Incorrecto"}</p>
              <p className="text-sm leading-relaxed">{currentQuestion.explanation}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
