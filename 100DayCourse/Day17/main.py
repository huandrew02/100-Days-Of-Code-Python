from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q_and_a in question_data:
    question_text = q_and_a["text"]
    question_answer = q_and_a["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("END OF QUIZ")
print(f"FINAL SCORE: {quiz.score}/{quiz.question_number}")