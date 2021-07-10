# Random for computer player picks
import random


def player_choice(user_choice):  # Register and shows the players choice
    if user_choice == 1:
        print("The player chose rock ")
    elif user_choice == 2:
        print("The player chose paper ")
    else:
        print("The player chose scissors ")


def computer_choice(cpu_choice):  # Register and shows the cpus choice
    if cpu_choice == 1:
        print("The computer chose rock ")
    elif cpu_choice == 2:
        print("The computer chose paper ")
    else:
        print("The computer chose scissors ")


def result(user_choice, cpu_choice, player_score, cpu_score): 
    if user_choice == cpu_choice:
        return [player_score + 0.5, cpu_score + 0.5]
    elif user_choice == 1 and cpu_choice == 3:
        return [player_score + 1, cpu_score]
    elif user_choice == 2 and cpu_choice == 1:
        return [player_score + 1, cpu_score]
    elif user_choice == 3 and cpu_choice == 2:
        return [player_score + 1, cpu_score]
    else:
        return [player_score, cpu_score + 1]


def print_score(p_score, c_score):  # the result and print the total score
    print("Score:""\nPlayer: ", p_score, "\nComputer: ", c_score)


def validation_input():  # Validate the input
    while True:
        try:
            user_input = int(input("Put your choice: "))
            if user_input not in range(1, 4):
                print("We only accept commands between 1 and 3, according to the table, type again ")
                continue
            if type(user_input) == int:
                break
        except ValueError:
            print("We only accept exact numbers ")
            continue
    return user_input


print('''1 - Rock
2 - Paper
3 - Scissors''')  # Printing the instructions
human_score = 0
computer_score = 0
while True:  # The condition is not important since the loop will stop on line 68 if the user wishes so
    user = validation_input()
    player_choice(user)
    ai = random.randint(1, 3)
    computer_choice(ai)
    human_score, computer_score = result(user, ai, human_score, computer_score)  # Accumulate the score
    print_score(human_score, computer_score)
    command = (input("Type q to stop the program, type any another number to keep playing "))
    if command == 'q':
        break