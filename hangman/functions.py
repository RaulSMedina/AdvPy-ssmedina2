import random

def random_word():# grabs random word from the text file

    f=open("words.txt","r")
    word=f.readlines()
    rw=random.randint(0,(len(word)-1))
    f.close()
    return word[rw].upper().strip()#returing the the word in all caps and getting read of all the whitespace

def game(word):#this the main game I used https://www.youtube.com/watch?v=pFvSb7cb_Us and geek for geeks to help make the code below 
    answer="_" * (len(word))
    guess=False
    guessL=[] #Holds letters guessed
    guessW=[] #Holds words guessed
    attempts=6
    print(hangman_visuals(attempts))
    print(answer)
    while not guess and attempts > 0:
        guessU = input("Enter your guess(Letter or Word): ").upper()
        if len(guessU)==1 and guessU.isalpha():
            if guessU in guessL:
                print("Letter ",guessU, " already guessed")
            elif guessU not in word:
                print("The letter ",guessU," is not in the word")
                attempts-=1
                guessL.append(guessU)
            else:
                print("Good guess. Letter ",guessU," is in the word")
                guessL.append(guessU)
                wholeWord=list(answer)
                index1=[i for i, letter in enumerate(word) if letter==guessU]
                for index2 in index1:
                    wholeWord[index2]=guessU
                answer="".join(wholeWord)
                if "_" not in answer:
                    guess=True
        elif len(guessU)==(len(word)) and guessU.isalpha():
            if guessU in guessW:
                print("The Word ",guessU," already guessed")
            elif guessU!=word:
                print("The Word ",guessU," is not the word")
                attempts-=1
                guessW.append(guessU)
            else:
                guess=True
                answer=word
        else:
            print("Invalid guess") 
        print(hangman_visuals(attempts))
        print(answer) 
    if guess:
        print("Hooray! You guess the corect word")
    else:
        print("You have ran out of tries. The word was " + word + ". Try agian")
    get_stats()

def get_stats():
    profile=input("Enter your new player profile name: ")
    stat=input("Did you win the game y or n ")
    if stat=='y':
        f=open(f"{profile}.txt",'a')
        f.write(", You won a game, ")
    else:
        f=open(f"{profile}.txt",'a')
        f.write(", You lost a game, ")

def player_stats():
    fileN=input("Please enter your new player profile name to see your stats. ")
    f=open(f"{fileN}.txt",'r')
    stats=f.readlines()
    print(stats)


def new_player():#creates a new player for the game
    name=input("Enter name of newplayer: ")
    f=open(f"{name}.txt",'a')
    f.write(name)
    f.write("'s Hangman Stats ")
    print("Player ",name," profile created")


def gameMenu():#main menu to navigate the game
    print("[1]Play game")
    print("[2]Display player stats")
    print("[3]Create a new player profile")
    print("[0] Quit game")
    option=int(input("Enter your option from above: "))
    if option==1:
        word=random_word()
        game(word)
        gameMenu()
    elif option==2:
        player_stats()
        gameMenu()
    elif option==3:
        new_player()
        gameMenu()
    elif option==0:
        print("Thanks for playing")
    else: 
        print("You choose an invaild option try agian")
        gameMenu()



def hangman_visuals(attempts):# a diagram for all the visuals of hangmman 
    visuals=[   """
                   ----------
                   |        |
                   |        o
                   |       \\|/
                   |        |
                   |       / \\
                   _
                """
                   ,
                """
                   ----------
                   |        |
                   |        o
                   |       \\|/
                   |        |
                   |       /
                   _
                """
                   ,
                """
                    ----------
                    |        |
                    |        o
                    |       \\|/
                    |        |
                    |
                    _
                """
                   ,
                """
                    ----------
                    |        |
                    |        o
                    |       \\|
                    |        |
                    _
                """
                    ,
                """
                    ----------
                    |        |
                    |        o
                    |        |
                    |        |
                    |        
                    _
                """
                    ,
                """
                    ----------
                    |        |
                    |        o
                    |
                    |
                    |
                    _
                """
                    ,
                """
                    ----------
                    |        |
                    |
                    |
                    |
                    |
                    _
                """
    ]
    return visuals[attempts]