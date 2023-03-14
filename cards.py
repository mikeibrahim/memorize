from card import Card
import random

class Cards:
    def __init__(self, name: str, cards: list = []):
        self.name = name
        self.cards = cards
        self.import_cards(name)

    def import_cards(self, file_path: str):
        self.cards = []
        with open(file_path, "r") as f:
            for line in f:
                question, answer = line.split(",")
                answer = answer.strip()
                self.add_card(question, answer)

    def add_card(self, question: str, answer: str):
        self.cards.append(Card(question, answer))

    def remove_card(self, card: Card):
        for card in self.cards:
            if card == card:
                self.cards.remove(card)

    def edit_answer(self, question: str, answer: str):
        for card in self.cards:
            if card.question == question:
                card.answer = answer

    def edit_question(self, question: str, new_question: str):
        for card in self.cards:
            if card.question == question:
                card.question = new_question

    def shuffle_cards(self):
        return random.shuffle(self.cards)

    def print_cards(self):
        print(f"Cards: {self.name}")
        for card in self.cards:
            print(card)
    
    def copy(self):
        return Cards(self.name, self.cards.copy())

    def splice(self, start: int, end: int):
        self.cards = self.cards[start:end]

    def __str__(self):
        return f"Cards: {self.name}: {self.cards}"

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]
    
    def __setitem__(self, index, value):
        self.cards[index] = value

    def __iter__(self):
        return iter(self.cards)

    def __contains__(self, question: str):
        for card in self.cards:
            if card.question == question:
                return True
        return False