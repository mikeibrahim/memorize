import os

def wipe_page():
    os.system("cls" if os.name == "nt" else "clear")

formattings = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "italic": "\033[3m",
    "strikethrough": "\033[9m"
}
text_colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m"
}
bg_colors = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m"
}

def plus_text(text: str, text_color: str = None, bg_color: str = None, formatting: str = None):
    return f"{text_colors[text_color] if text_color in text_colors else ''}{bg_colors[bg_color] if bg_color in bg_colors else ''}{formattings[formatting] if formatting in formattings else ''}{text}{formattings['reset']}"

def print_plus(text: str, text_color: str = None, bg_color: str = None, formatting: str = None):
    print(plus_text(text, text_color, bg_color, formatting))

def input_plus(text: str, text_color: str = None, bg_color: str = None, formatting: str = None):
    return input(plus_text(text, text_color, bg_color, formatting))
