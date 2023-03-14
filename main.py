from cards import Cards
from study_session import StudySession
import sys
import readline
import os

valid_inputs = [f for f in os.listdir("cards") if os.path.isfile(os.path.join("cards", f))] + ["cards"]
def completer(text, state):
    options = [i for i in valid_inputs if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

def __main__():
    card_path = sys.argv[1]
    cards = Cards(card_path)
    study_session = StudySession(cards)
    study_session.start()

if __name__ == "__main__":
    __main__()