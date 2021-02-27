print("Welcome to my Rock, Paper, Scissors Game!")

state = False
get_number_of_games = 3
illegal_value = "ilelgal value"


def set_int(x):
    try:
        return int(x)
    except ValueError:
        return False


while not state:
    get_number_of_games = set_int(input("Enter the number of games to play -- odd number 3 to 11: "))
    if not set_int(get_number_of_games):
        print(illegal_value)
        continue
    elif set_int(get_number_of_games) % 2 == 0:
        print(illegal_value)
        continue
    elif set_int(get_number_of_games) < 3 or set_int(get_number_of_games) > 11:
        print(illegal_value)
        continue
    state = True


def get_option(game_turn):
    ask_again = False
    while not ask_again:
        print(f"Game {game_turn + 1}")
        option = input("Enter (R)ock, (P)aper, or (S)cissors: ")
        option = option.upper()
        if option == 'R' or option == "P" or option == 'S':
            return option
        else:
            print("Unknown selection. Try again\n")
            continue


for i in range(0, get_number_of_games):
    get_option(i)
    print('\n')
