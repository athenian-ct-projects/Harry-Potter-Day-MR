print("Harry Potter Day Board Game \nBy MR '23 \n Instructions: Enter "Dice" to roll the dice or "Card" to pick a card.")

def trivia():
 #This function is to ask the person trivia. If they get it right, then nothing happens. If they get it wrong, they are asked a new question.   
   #The part below makes it so that if they get the answer wrong, then they must do a new question.
    c = False
    while (c != True):
        import random
        Card = random.randint (1, 6)
        if Card == (1):
          #This is the first question
            x = input ("Who is the main character? )
            if x == ("Harry Potter"):
                print ("True")
                #Below, this makes it so that if you get the answer right, the function ends
                c = True
            else:
                print ("False")
        if Card == (2):
            #Second question
            y = input ("Who is the 'Brightest Wizard of the century' as proclaimed by Harry? )
            if y == ("Hermione Granger"):
                print ("True")
                #Below, this makes it so that if you get the answer right, the function ends
                c = True
            else:
                print ("False")
        if Card == (3):
            #Third question
            z = input ("What House is Harry Part Of? )
            if z == ("Gryffindor"):
                print ("True")
                #Below, this makes it so that if you get the answer right, the function ends
                c = True
            else:
                print ("False")
        if Card == (4):
          #question four
            a = input ("How old is Harry Potter at the Beginning of the Story? ")
            if a == ("12"):
                print ("True")
               #Below, this makes it so that if you get the answer right, the function ends
                c = True
            else:
                print ("False")
        if Card == (5):
            #Fifth question
            b = input ("Who is Harry Potter's Best Friend? ")
            if b == ("Ron Weasly"):
                print ("True")
                #Below, this makes it so that if you get the answer right, the function ends
                c = True
            else:
                print ("False")
        if Card == (6):
            l = input ("How many points do you get for catching the golden snitch in a game of Quidditch? ")
            if l == ("150"):
                print ("True")
                c = True
            else:
                print ("False")

def dice ():
    #This is a function for a randomizer. The randomizer is the equivilent of a dice. 
    #With the number you got, comes a horcrux, and they are in the order of destruction.
    import random
    Dice = random.randint (1, 7)
    #Each of the numbers in the randomizer is a variable corresponding to an ammount to move foward
    if Dice == (1):
        print ("You Found Tom Riddle's Diary. Move One Space")
    if Dice == (2):
        print ("You Found Marvolo Gaunt's ring. Move Two Spaces")
    if Dice == (3):
        print ("You Found Salazar Slytherin's locket. Move Three Spaces")
    if Dice == (4):
         print ("You Found Helga Hufflepuff's cup. Move Four Spaces")
    if Dice == (5):
        print ("You Found Rowena Ravenclaw's diadem. Move Five Spaces")
    if Dice == (6):
        f = input("You Foud Nagini, the snake. Do you kill it or run away? ")
        if f == ("Kill"):
            print ("You advance 6 spaces")
        else:
            print ("You Died. Sad face. Stay Where You Are")   
    if Dice == (7):
         print ("You Found Harry Potter. You move foward 7 spaces.")


def yellow ():
    #This function is for when you land on yellow squares
    #when you land on a yellow square, the randomizer chooses a for loop to denote how many spaces to move back
    import random
    Yellow = random.randint (1,3)
    if Yellow == (1):
        for m in range (1,2):
            print (m)
    if Yellow == (2):
        for n in range (3,4):
            print (n)
    if Yellow == (3):
        for o in range (5,6):
            print (o)   

d = input ("Dobby Is So Happy To Meet You! Dobby wants to know if you want anything. (Type 'Dice' or 'Card'. If you land on a yellow space, type 'Yellow')")
if d == ("Card"):
    trivia()
#The function above calls the trivia
if d == ("Dice"):
    dice ()
#The function above calls the dice randomizer    
if d == ("Yellow"):
    yellow ()         
#The function above calls the function that denotes how many spaces to move back
