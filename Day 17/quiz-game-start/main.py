from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for entry in question_data:
    question_text = entry["question"]
    question_answer = entry["correct_answer"]  
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.nextQuestion()

print("You have finished the quiz!")
print(f"Your score was: {quiz.user_score} / {quiz.question_number}")