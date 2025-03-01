'''
 1 for snake
 -1 for water
 0 for gun

'''
import random
computer= random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"snake":1,"water":-1,"gun":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you = youDict[youstr]
print(f"you chose {reverseDict[you]} \n computer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a tie")
else:
    if (you == 1 and computer == -1):
        print("You win!")
    elif (you == -1 and computer == 0):
        print("You win!")
    elif (you == 0 and computer == 1):
        print("You win!")
    elif (you == -1 and computer == 1):
        print("You lose!")
    elif (you == 0 and computer == -1):
        print("You lose!")
    elif (you == 1 and computer == 0):
        print("You lose!")
    elif (you == 1 and computer == 0):
        print("You lose!")
    elif (you == 0 and computer == 1):
        print("You lose!")
    elif (you == -1 and computer == 0):
        print("You lose!")
    elif (you == 0 and computer == 1):
        print("You lose!")
    elif (you == 1 and computer == -1):
        print("You lose!")
    elif (you == -1 and computer == 0):
        print("You lose!")
    else:
        print("something went wrong") 
# this code has uneccessary elif statements
#let us look at a simplified version of the code below
import random
computer= random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"snake":1,"water":-1,"gun":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you = youDict[youstr]
print(f"you chose {reverseDict[you]} \n computer chose {reverseDict[computer]}")


if computer == you:
    print("It's a tie")
elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
    print("You win!")
else:
    print("You lose!")

    
