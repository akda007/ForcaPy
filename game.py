from sys import stdin
from utils import *

def hide_word(word, guessed):
    hidden = ''
    for c in word:
        if c in guessed or c.isspace():
            hidden += c
            continue
        hidden += '_'
    return hidden

class Forca:
    guessed_all = ""
    guessed = ""
    
    def __init__(self, word, lives):
        self.word, self.lives = word, lives
        screen_clear()
        cursor_home()
        
    def start(self):
        def draw_ui():
            cursor_to(0, 0)
            line_clear()
            
            printf("\n\nWord: {}\t\tRemaining Lives: {}\tGuessed: {}".format(hide_word(self.word, self.guessed), self.lives, self.guessed_all))
    
        def get_input():
            cursor_down(1)
            
            printf("\rYour Guess: ")
            line_clear_end()

            return input()[0]
            
        
        while True:
            draw_ui()

            if self.lives == 0:
               return False

            completed = lambda a, b: sorted(set(a)) == sorted(set(b))
            
            if completed(self.guessed, self.word):
               return True

            guess = get_input()
           
            if guess in self.guessed_all:
                continue
           
            self.guessed_all += guess
           
            if guess in self.word:
                self.guessed += guess
            else:
                self.lives -= 1