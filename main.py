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
for i in range(0, get_number_of_games):
    print(f"This is game {i + 1}")
