import random

# read and split file
f= open("quiz_questions_answers.txt", "r")
file=f.read().split("\n")

ct=0 # num of questions/respones
dict={} 

# split into questions and answers and store in dict
for i in file:
    fy=i.strip().split("-")
    if len(fy)==2:
        dict[fy[0]]=fy[1].strip()
        ct+=1

# player variables
p1=True
player1=0
player2=0
game=True

print("Welcome Players! Here is a game for you...")

# runs game
while game: 
    question=random.choice(list(dict.keys()))

    # player pts
    print("Player 1: ", player1)
    print("Player 2: ", player2)
    print(question)

    #p1 turn
    if p1:
        guess=input("Player 1, please proceed to answer?")
        if guess.lower()==dict[question].lower():
            print("Correct")
            player1+=10
        else:
            print("Incorrect")
    # p2 turn
    else:
        guess=input("Player 2, please proceed to answer?")
        if guess.lower()==dict[question].lower():
            print("Correct")
            player2+=10
        else:
            print("Incorrect")
    
    # final winner
    if player1==30 or player2==30:
        game=False
        if p1:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    
    #switch players
    p1=not p1


    

