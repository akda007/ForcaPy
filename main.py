import random as rd
import game
import sys


def load_words(file = "words.txt"):
    f = open(file, "r")
    return f.readlines()
    

def main():
    words = load_words()

    while True:
        word = words[rd.randint(0, len(words))].replace('\n', '')
        
        g = game.Forca(word, 5)
        res = g.start()

        if res:
            print("\n\nCongratulations!\nYou Won!")
        else:
            print("\n\nGAME OVER!!\nThe word was %s" % word)
            
        print("Play again? (y, n)")
        choice = input()
        
        if choice == 'n':
            break
        

if sys.platform == "win32":
    import ctypes
    kernel = ctypes.windll.kernel32
    kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)
    

if __name__ == "__main__":
    main()
