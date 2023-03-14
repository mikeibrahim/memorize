from card import Card
from cards import Cards
import random
from pretty import *

class StudySession:
    def __init__(self, cards: list):
        self.cards = cards
        self.current_session = None
        self.study_terms = None
        self.random = None

    def page_title(self, current_num, final_num):
        return f"{self.current_session} ({current_num}/{final_num})"

    def start(self):
        wipe_page()
        print_plus("Welcome to the Study App!", "green", "", "bold")
        print("1) Flashcards")
        print("2) Multiple Choice")
        print("3) Writing")
        print("4) Switch Cards")
        print("5) Quit")

        self.current_session = None
        self.study_terms = None
        self.random = None

        page = -1
        while page < 1 or page > 5:
            page = input_plus("Select a page: ")
            if not page.isdigit():
                page = -1
            else:
                page = int(page)
        
        if page < 4:
            while self.study_terms == None:
                self.study_terms = input_plus("Do you want to study the terms or definitions? (t/d): ", "", "", "italic").lower()
                if self.study_terms != "t" and self.study_terms != "d":
                    self.study_terms = None
                else:
                    self.study_terms = self.study_terms == "t"

            while self.random == None:
                self.random = input_plus("Do you want to study in random order? (y/n): ", "", "", "italic").lower()
                if self.random != "y" and self.random != "n":
                    self.random = None
                else:
                    self.random = self.random == "y"

        if page == 1:
            self.flashcards()
        elif page == 2:
            self.multiple_choice()
        elif page == 3:
            self.writing()
        elif page == 4:
            self.switch_cards()
        elif page == 5:
            return
        
        self.start()

    def flashcards(self):
        self.current_session = "Flashcards"
        cards = self.cards

        if self.random:
            cards = self.cards.copy()
            cards.shuffle_cards()
        
        studying = True
        while studying:
            for i, card in enumerate(cards):
                wipe_page()
                print_plus(self.page_title(i + 1, len(cards)), "blue",'','bold')
                print(card.question if self.study_terms else card.answer)
                
                input_plus("See answer? [Enter]", "", "", "italic")
                print(card.answer if self.study_terms else card.question)

                if (i < len(cards) - 1):
                    input_plus("See next card? [Enter]", "", "", "italic")
            
            studying = "y" in input_plus("Do you want to study again? (y/n): ", "", "", "italic").lower()


    def multiple_choice(self, numChoices: int = 4):
        self.current_session = "Multiple Choice"
        cards = self.cards

        if self.random:
            cards = self.cards.copy()
            cards.shuffle_cards()
        
        studying = True
        while studying:
            for i, card in enumerate(cards):
                wipe_page()
                print_plus(self.page_title(i + 1, len(cards)), "blue",'','bold')
                print(card.question if self.study_terms else card.answer)
                
                multiple_choice = cards.copy()
                multiple_choice.remove_card(card)
                multiple_choice.shuffle_cards()
                multiple_choice.splice(0, numChoices)
                multiple_choice[random.randint(0, numChoices - 1)] = card

                for i, choice in enumerate(multiple_choice):
                    print(f"{i + 1}) {choice.answer if self.study_terms else choice.question}")
                
                response = -1
                while response < 0 or response > numChoices - 1:
                    response = input_plus(f"Check answer? (1-{numChoices}): ", "", "", "italic")
                    if not response.isdigit():
                        response = -1
                    else:
                        response = int(response) - 1
                
                if multiple_choice[response] == card:
                    print("Correct!, it is", card.answer if self.study_terms else card.question)
                else:
                    print("Incorrect!, it is", card.answer if self.study_terms else card.question)
                
                if (i < len(cards) - 1):
                    input_plus("See next card? [Enter]", "", "", "italic")
            studying = "y" in input_plus("Do you want to study again? (y/n): ", "", "", "italic").lower()
    

    def writing(self):
        self.current_session = "Writing"
        cards = self.cards

        if self.random:
            cards = self.cards.copy()
            cards.shuffle_cards()
        
        studying = True
        while studying:
            for i, card in enumerate(cards):
                wipe_page()
                print_plus(self.page_title(i + 1, len(cards)), "blue",'','bold')
                print(card.question if self.study_terms else card.answer)

                response = input_plus("Answer: ", "", "", "italic")
                
                if response == (card.answer if self.study_terms else card.question):
                    print("Correct!")
                else:
                    print("Incorrect!, it is", card.answer if self.study_terms else card.question)
                
                if (i < len(cards) - 1):
                    input_plus("See next card? [Enter]", "", "", "italic")
            studying = "y" in input_plus("Do you want to study again? (y/n): ", "", "", "italic").lower()
    
    def switch_cards(self):
        # recieve a new path for the cards
        path = input_plus("Enter the filepath to the cards: ", "", "", "italic")
        self.cards = Cards(path)
        print("Cards have been switched: ", self.cards)