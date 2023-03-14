# Study app in the terminal
# Kind of like Quizlet but in the terminal

class Card:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def __str__(self) -> str:
        return f"Question: {self.question}"

    def __eq__(self, other):
        return self.question == other.question and self.answer == other.answer
    
    def __repr__(self):
        return f"({self.question}, {self.answer})"