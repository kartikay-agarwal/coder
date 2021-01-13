import random
import time
game_list = ['Rock', 'Paper' , 'Scissors']
computer = c = 0
command = p = 0
print("Score: Computer" + str(c) + "Player" + str(p))
# the loop
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Rock, Paper , Scissors or Quit: ")
    if command == computer_choice:
        print("tie")
    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print("Player won!")
            print("Player: " + command)
            print("Computer: " + computer_choice)
            p += 1
        else:
            print("Computer won!")
            print("Player: " + command)
            print("Computer: " + computer_choice)
            c +=1
    elif command == 'Paper':
        if command == 'Rock':
            print("Player won!")
            print("Player: " + command)
            print("Computer: " + computer_choice)
            p += 1
        else:
            print("Computer won!")
            print("Player: " + command)
            print("Computer: " + computer_choice)
            c += 1
    elif command == 'Scissors':
        if computer_choice == 'Paper':
            print("Player won!")
            print("Player: " + command)
            print("Computer: " + computer_choice)
            p += 1
        else:
            print("Computer won!")
            print("Player: " + command)
            print("Computer: " + computer_choice)
            c += 1
    elif command == 'Quit':
        print("Score: Computer " + str(c) + " Player " + str(p))
        time.sleep(3)
        break
    else:
        print("Wrong command!")
print("Player: " + command)
print("Computer: " + computer_choice)
print("")
print("Score: Computer " + str(c) + " Player " + str(p))
print("")

