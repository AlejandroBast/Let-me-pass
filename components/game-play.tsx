"use client"

import { useState, useEffect } from "react"
import type { Module } from "@/app/page"
import { Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Progress } from "@/components/ui/progress"
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
    if (!currentQuestion || !userAnswer.trim() || isAnswering) return

    setIsAnswering(true)
    const isCorrect = checkAnswer(currentQuestion, userAnswer)
    setFeedback(isCorrect ? "correct" : "incorrect")

    if (isCorrect) {
      setScore(score + 1)
      setBridgeProgress((questionNumber / totalQuestions) * 100)
    }

    setTimeout(() => {
      if (questionNumber >= totalQuestions) {
        onComplete(score + (isCorrect ? 1 : 0), totalQuestions)
      } else {
        setQuestionNumber(questionNumber + 1)
        setCurrentQuestion(generateQuestion(module))
        setUserAnswer("")
        setFeedback(null)
        setIsAnswering(false)
      }
    }, 2000)
  }

  if (!currentQuestion) return null

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="flex justify-between items-center mb-6">
          <Button variant="outline" onClick={onBackToMenu}>
            ← Volver al Menú
          </Button>
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
          <Progress value={((questionNumber - 1) / totalQuestions) * 100} className="h-2" />
        </div>

        {/* Question Card */}
        <Card className="p-8 border-2 border-border animate-in fade-in slide-in-from-bottom-4">
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
                <Button
                  key={index}
                  variant={userAnswer === option ? "default" : "outline"}
                  className="w-full justify-start text-left h-auto py-4 px-6"
                  onClick={() => setUserAnswer(option)}
                  disabled={isAnswering}
                >
                  {option}
                </Button>
              ))}
            </div>
          ) : (
            <Input
              type="text"
              placeholder="Escribe tu respuesta..."
              value={userAnswer}
              onChange={(e) => setUserAnswer(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
              disabled={isAnswering}
              className="text-lg p-6"
            />
          )}

          <Button
            onClick={handleSubmit}
            disabled={!userAnswer.trim() || isAnswering}
            className="w-full mt-6 text-lg py-6"
            size="lg"
          >
            {isAnswering ? "Verificando..." : "Enviar Respuesta"}
          </Button>

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
        </Card>
      </div>
    </div>
  )
}
