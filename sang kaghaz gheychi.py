
from random import choice

plays = ['Rock', 'Paper', 'Scissors']
computer_score = 0
player_score = 0

computer = choice(plays)
player = input('Rock, Paper, Scissors?(End to Quit.)\n')


while player != 'End':


    print('Computer:', computer)
    print('Player  :', player)


    if player == computer:
        print("Tie!\n")

    elif player == "Rock":
        if computer == "Paper":
            print("Computer wins!\n")
            computer_score += 1
        else:
            print("Player wins!\n")
            player_score += 1

    elif player == "Paper":
        if computer == "Scissors":
            print("Computer Wins!\n")
            computer_score += 1
        else:
            print("Player Wins!\n")
            player_score += 1

    elif player == "Scissors":
        if computer == "Rock":
            print("Computer Wins!\n")
            computer_score += 1
        else:
            print("Player Wins!\n")
            player_score += 1


    else:
        print("That's not a valid play.\n")

  
    computer = choice(plays)
    player = input('Rock, Paper, Scissors?(End to Quit.)\n')


print('Game Over!')
print('Computer Score: ', computer_score)
print('Player Score  : ', player_score)
