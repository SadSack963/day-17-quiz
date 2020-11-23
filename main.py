from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects called question_bank
question_bank = []
for question in question_data:
    new_q = Question(q_text=question["question"], q_answer=question["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

# print("You've completed the quiz.")
# print(f"You're final score is {quiz.score} / {quiz.question_number}")
