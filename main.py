import random
from question_model import Question
from data import question_data
from quiz_brain import QuiZBrain

question_bank = []
for item in question_data:
    question = Question(q_text=item["text"],q_answer=item["answer"])
    question_bank.append(question)
quiz = QuiZBrain(q_list=question_bank)
while quiz.still_have_question():
    quiz.next_question()
print("You have completed the Quiz :")
print(f"your final score is {quiz.score}/12")



