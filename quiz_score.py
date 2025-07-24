import time
from quiz import Kana_quiz

# Class function to display the quiz score
class QuizScore():
    def __init__(self, correct_answers, total_questions):
        self.correct_answers = correct_answers
        self.total_questions = total_questions

    def score_display(self):
        print(f"You have answered {self.correct_answers} out of {self.total_questions} questions correctly.")
        score = (self.correct_answers / self.total_questions) * 100
        print(f"Your quiz score is: {score}%")
        time.sleep(1)
        print("Thank you for taking the quiz! Goodbye. クイズをしてくれてありがとうございました! さよなら。") 

        if score == 0:
            print("You did not answer any questions correctly. Please try again after revision.")
            print("Good luck for next time!")
            return

        elif score < 50 and score > 0:
            print("You answered less than half of the questions correctly. Please try again after revision.")
            print("Good luck for next time!")
            return

        elif score > 50 and score <= 90:
            print("You answered more than half of the questions correctly. Good job! よくできました！")
            print("Keep practicing to get full marks!")
            return

        elif score == 100:
            print("Congratulations! You answered all questions correctly.")
            print("おめでとうございます！ よくできました。")

