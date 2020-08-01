# Created on 31- Aug- 2020
# Created By: Ashutosh Kamboj and Nandini Goyal

import random
from word import word_list   # The word file is already created to get the names of the elments to guess.



def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_complition ="_" * len(word)
    guessed = False
    guessed_letters= []
    guessed_words= []
    tries= 6
    print(" Lets play Hangman")
    print(display_hangman(tries))
    print(word_complition)
    print("\n")
    while not guessed and tries > 0:
        guess = input(" Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already gussed the letter",guess)
            elif guess not in word:
                print(guess,"is not in the word.")
                tries -=1
                guessed_letters.append(guess)
            else:
                print("Goood job",guess, "is the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_complition)
                indices = [i for i ,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] =  guess
                word_complition= "".join(word_as_list)
                if "_" not in word_complition:
                    guessed=True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                prinnt("You alreay guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -=1
                guessed_words.append(guess)
            else:
                guessed=True
                word_complition=word
        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_complition)
        print("\n")
    if guessed:
        print("Congrats, You saved the Man.")
    else:
        print("Ooops!! You Ran Out Of tries. YOUR MAN DIED.  The word was "+word+" \nTRY NEXT TIME.")




def display_hangman(tries):
    stages = [""" 
                 ---------
                 |        |
                 |
                 |
                 |
                 |
            -----|"""

            ,""" 
                 ---------
                 |        |
                 |        O
                 |
                 |
                 |
            -----|"""
              ,""" 
                 ---------
                 |        |
                 |        O
                 |        |
                 |        |
                 |
            -----|""","""
                 ---------
                 |        |
                 |        O
                 |       \\|
                 |        |
                 |
            -----|
            """,
            """
                             ---------
                             |        |
                             |        O
                             |       \\|/
                             |        |
                             |
                        -----|
                        """
    ,"""
                 ---------
                 |        |
                 |        O
                 |       \\|/
                 |        |
                 |       /
            -----|
            """
            ,
              """
                               ---------
                               |        |
                               |        O
                               |       \\|/
                               |        |
                               |       / \\
                          -----|
                          """
    ]
    return stages[tries]

def main():
    word=get_word()
    play(word)
    while input("Try Again? (Y/N)").upper() =="Y":
        word=get_word()
        play(word)

if __name__ == '__main__':
    main()
