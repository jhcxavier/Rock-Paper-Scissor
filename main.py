import random

print("Welcome to my Rock, Paper, Scissors Game!")

state = False
get_number_of_games = 3
illegal_value = "illegal value"
unknown_value = "Unknown selection. Try again\n"
number_of_plays = "Enter the number of games to play -- odd number 3 to 11: "
min_play = 3
max_play = 11


def set_int(x):
    try:
        return int(x)
    except ValueError:
        return False


while not state:
    get_number_of_games = set_int(input(number_of_plays))
    if not set_int(get_number_of_games):
        print(illegal_value)
        continue
    elif set_int(get_number_of_games) % 2 == 0:
        print(illegal_value)
        continue
    elif set_int(get_number_of_games) < min_play or set_int(get_number_of_games) > max_play:
        print(illegal_value)
        continue
    state = True

player_score = list()
computer_score = list()


def convert_score(score):
    if score == "R":
        return 0
    elif score == "P":
        return 1
    elif score == "S":
        return 2


def get_option(game_turn):
    ask_again = False
    while not ask_again:
        print(f"Game {game_turn + 1}")
        option = input("Enter (R)ock, (P)aper, or (S)cissors: ")
        option = option.upper()
        if option == 'R' or option == "P" or option == 'S':
            player_score.append(convert_score(option))
            return option
        else:
            print(unknown_value)
            continue


def computer_choice():
    computer_turn = random.randint(0, 2)
    if computer_turn == 0:
        computer_score.append(0)
        print("Computer chose Rock")
    elif computer_turn == 1:
        computer_score.append(1)
        print("Computer chose Paper")
    elif computer_turn == 2:
        computer_score.append(2)
        print("Computer chose Scissors")


def get_winner(player, computer):
    if player == computer:
        print("This game is a draw")
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("Computer wins")
    elif (player == 1 and computer == 0) or (player == 2 and computer == 1) or (player == 0 and computer == 2):
        print("Player wins")


for i in range(0, get_number_of_games):
    get_option(i)
    computer_choice()
    get_winner(player_score[i], computer_score[i])
    print('\n')
