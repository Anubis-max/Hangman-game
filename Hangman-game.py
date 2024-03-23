import random
import time

words = ["apple", "banana", "mango", "strawberry", "orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon", "cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]
word = random.choice(words)
chances = int(len(word) / 2)
guesses = ""
failed = 0
guess = ""

class Hangman:
    def counter():
        print("Game begins in 3!")
        time.sleep(1)
        print("Game begins in 2!")
        time.sleep(1)
        print("Game begins in 1!")
        time.sleep(1)
        return ""

    def player():
        global guesses
        global failed
        global guess
        guess = input("enter the letter: ")
        if len(guess) != 1:
            print("Error: Enter a single letter.")
            return
        if guess.isalpha() == False:
            print("Error: Enter a letter.")
            return
        guesses += guess
        if guess not in word:
            failed += 1
            Hangman.lose()  


    def checks():
        global guesses
        global failed
        global word
        display = ""  
        for char in word:
            if char in guesses:
                display += char + " "
            else:
                display += "_ "
        return display 


    def win():
        global failed
        if "_" not in Hangman.checks():
            print("\nCongratulations! You won!")
            return True
        return False


    def lose():
        global chances
        global guess
        if guess not in word:
            chances -= 1
            print(f"\nWrong letter! You have {chances} tries left.")

print(Hangman.counter())
while chances > 0:
    print(Hangman.checks())
    Hangman.player()
    if Hangman.win():
        break
    if chances == 0:
        print("You lost! You don't have tries anymore.")
        break