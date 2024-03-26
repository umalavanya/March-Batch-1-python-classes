# Rock-Paper-Sisscors Game
# Paper - Sisscors  --> Sisscors
# Rock - Sisscors   --> Rock
# Paper - Rock      --> Paper

import random
import asciitext as at

print("----------------------------------------------------------------------")

print(at.text)

print("----------------------------------------------------------------------")

list1 = ["rock","paper", "sis"]
computer_choice = random.choice(list1)

total_count = 0
user_won_count = 0
computer_won_count = 0
draw_count = 0

quit = "y"

while quit == "y" :
    
    user_choice = input("Enter your choice (rock, paper, sis) :")
    print("------------------------------------------")
    print(f"computer choice: {computer_choice}    ", end=" ")
    print(f"user choice: {user_choice}")
    print("------------------------------------------")
    if (computer_choice == 'paper' ):
        if ( user_choice == 'paper') :
            print("Draw!")
            draw_count +=  1
            
        elif ( user_choice == 'rock') :
            print("You Won!")
            user_won_count += 1
        else:
            print("computer Won!")
            computer_won_count += 1
            
    if (computer_choice == 'rock' ):
        if ( user_choice == 'paper') :
            print("You won!")
            user_won_count += 1
            
        elif ( user_choice == 'rock') :
            print("Draw!")
            draw_count +=  1
        else:
            print("computer Won!")
            computer_won_count += 1
            
    if (computer_choice == 'sis' ):
        if ( user_choice == 'paper') :
            print("Computer won!")
            computer_won_count += 1
            
        elif ( user_choice == 'rock') :
            print("You won!")
            user_won_count += 1
        else:
            print("Draw!")
            draw_count +=  1
            
    total_count += 1
    print(f"computer won {computer_won_count} times")
    print(f"user won {user_won_count} times")
    print(f"draw {draw_count} times")       
    quit = input("Do you want to continue(y/n): ")
    
print(f"computer won {computer_won_count} times")
print(f"user won {user_won_count} times")
print(f"draw {draw_count} times") 


print(f"draw {total_count} times") 


if computer_won_count > user_won_count :
    print("Computer is the winner!")
    
elif computer_won_count == user_won_count :
    print("The game is draw!")
    
else:
    print("You are the Winner!")
    