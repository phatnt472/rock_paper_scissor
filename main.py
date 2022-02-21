import random 

def make_computer_choice():
    return  random.choice(["Rock","Paper","Scissor"])

def make_people_choice():
    dict_choices = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissor",
        "Q": "Quit"
    }
    people_choice = input('Enter your choice [R] Rock, [P] Paper,  [S] Scissor, [Q] Quit: ').upper()
    while people_choice not in list(dict_choices.keys()):
        print("Your choice is invalid!")
        people_choice = input('Enter your choice [R] Rock, [P] Paper,  [S] Scissor, [Q] Quit: ').upper()
    return dict_choices[people_choice]

def main():
    counter = 0
    while 1:
        counter += 1
        computer_choice = make_computer_choice()
        people_choice = make_people_choice()
        if  people_choice != "Quit":
            print(f"Game #{counter}")
            print(f'You choice: {people_choice} vs  The computer choice: {computer_choice}')
            if  people_choice == computer_choice:
                print('You and The computer are draw')
            elif (people_choice == "Rock" and computer_choice == "Paper") or (people_choice  == "Paper"and computer_choice == "Scissor") or (people_choice == "Scissor" and computer_choice == "Rock"):
                print("You lose and The computer wins")
            else:
                print("You win and The computer loses")
        else:
            print("Thanks for playing!")
            print("Have a nice day!")
            break

if __name__ == '__main__':
    main()