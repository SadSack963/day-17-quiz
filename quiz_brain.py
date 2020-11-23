class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Get ready for the next question
        choice = input(f"Q.{self.question_number}: {current_question.text} (True / False) : ")
        self.check_answer(answer=current_question.answer, choice=choice)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, choice, answer):
        if answer.lower() == choice.lower():
            print("Correct. ", end="")
            self.score += 1
        else:
            print("Wrong. ", end="")
        print(f"The answer was {answer}.")
        if self.still_has_questions():
            print(f"Current Score: {self.score} / {self.question_number}\n\n")
        else:
            print("\nYou've completed the quiz.")
            print(f"You're final score is  {self.score} / {self.question_number}")
