import string
import time
from termcolor import colored

p1_ship_lengths = [2, 3, 3, 4, 5]  # List of remaining ship lengths
p2_ship_lengths = [2, 3, 3, 4, 5]  # for both players

p1_grid = []  # Create battleship grid for player one
p1_opponent_grid = []  # Create grid of opponent's unknown board
for i in range(10):
    p1_grid.append(["-" for j in range(10)])
    p1_opponent_grid.append(["-" for j in range(10)])

p2_grid = []  # Create battleship grid for player two
p2_opponent_grid = []  # Create grid of opponent's unknown board
for i in range(10):
    p2_grid.append(["-" for j in range(10)])
    p2_opponent_grid.append(["-" for j in range(10)])


def print_board(board, color="white"):
    print(colored("    1    2    3    4    5    6    7    8    9    10\n", color))
    for row in range(10):
        print(colored(string.ascii_uppercase[row], color), end="")
        for col in range(10):
            print(colored("  " + str(board[row][col]) + " ", color), end="")
        print("\n")


def place_ship(grid, ship_lengths, ship_length, letter, number, orientation):
    row = ord(letter) - 65  # Convert position letter to row number
    col = number - 1  # Convert position number to column number
    print(str(row)+" "+str(col))
    is_space_for_ship = True
    if ship_length in ship_lengths:  # Make sure the currently playing player has the ship available

        if row <= 10 and row >= 0 and col <= 10 and col >= 0:  # Make sure row and column are inside bounds
            if orientation.lower() == "v" or orientation.lower() == "vertical":
                if row + ship_length <= 10:  # Make sure ship with given length will fit in grid
                    for i in range(row, row + ship_length):  # Iterate through all spaces the ship will take up,
                        if grid[i][col] == "-":  # and make sure they are empty
                            pass
                        else:
                            print("Something already exists at that position! Try again!")
                            is_space_for_ship = False
                            return False
                    if is_space_for_ship:
                        for i in range(row, row + ship_length):
                            grid[i][col] = "O"
                        ship_lengths.remove(ship_length)
                        return True
                else:
                    print("That position is out of bounds!")
                    return False
            if orientation.lower() == "h" or orientation.lower() == "horizontal":
                if col + ship_length <= 10:  # Make sure ship with given length will fit in grid
                    for i in range(col, col + ship_length):
                        if grid[row][i] == "-":
                            pass
                        else:
                            print("\nSomething already exists at that position! Try again!\n")
                            is_space_for_ship = False
                            return False
                    if is_space_for_ship:
                        for i in range(col, col + ship_length):
                            grid[row][i] = "O"
                        ship_lengths.remove(ship_length)
                        return True
                else:
                    print("That position is out of bounds!")
                    return False

        else:
            print("That position is out of bounds! Try again!")
            return False


def check_win(player_opponent_grid):  # Check if
    hit_count = 0
    for i in range(10):
        for j in range(10):
            if player_opponent_grid[i][j] == "X":
                hit_count += 1
    if hit_count >= 17:
        return True
    return False


def attack(opponent_grid, player_unknown_grid, letter, number):
    row = ord(letter) - 65
    col = number - 1
    status = opponent_grid[row][col]
    if status == "O":
        opponent_grid[row][col] = "X"
        player_unknown_grid[row][col] = "X"
        return "hit"
    elif status != "-":
        return "alreadyattacked"
    elif status == "-":
        opponent_grid[row][col] = "#"
        player_unknown_grid[row][col] = "#"
        return "miss"


# Examples of attack function:
# attack(player_two_grid, player_one_opponent_grid, "F", 5) - Player one's turn
# attack(player_one_grid, player_two_opponent_grid, "F", 5) - Player two's turn

print("Player 1's turn:\n")
print_board(p1_grid, "blue")

for i in range(5):
    print("Placing ship " + str(i + 1) + "...")
    while True:
        try:
            ships = ""
            for i in range(len(p1_ship_lengths)):
                ships += str(p1_ship_lengths[i])
                if i == len(p1_ship_lengths) - 1:
                    break
                ships += ", "
            length = int(input("Enter length of ship to place (Available ships: " + ships + "): "))
            if length not in p1_ship_lengths:
                print("\nYou have no ships of that length!\n")
                continue
        except ValueError:
            print("\nError! Enter an integer!\n")
            continue
        try:
            pos = input("Enter board position to place ship (eg B3): ")
            letter = list(pos)[0].upper()
            number = int(list(pos)[1])
        except:
            print("\nError! Enter the position correctly!\n")
            continue
        orientation = input("Place ship vertically or horizontally? (v/h) ").lower()
        if orientation != "v" and orientation != "vertical" and orientation != "h" and orientation != "horizontal":
            print("\nError! Enter a correct orientation!!\n")
            continue
        if place_ship(p1_grid, p1_ship_lengths, length, letter, number, orientation):
            print("Ship " + str(i + 1) + " placed.")
            print_board(p1_grid, "blue")
            break
print("All ships placed.\n")


print("Player 2's turn:\n")
print_board(p2_grid, "red")
for i in range(5):
    print("Placing ship " + str(i + 1) + "...")
    while True:
        try:
            ships = ""
            for i in range(len(p2_ship_lengths)):
                ships += str(p2_ship_lengths[i])
                if i == len(p2_ship_lengths) - 1:
                    break
                ships += ", "
            length = int(input("Enter length of ship to place (Available ships: " + ships + "): "))
            if (length not in p2_ship_lengths):
                print("\nYou have no ships of that length!\n")
                continue
        except ValueError:
            print("\nError! Enter an integer!\n")
            continue
        try:
            pos = input("Enter board position to place ship (eg B3): ")
            letter = list(pos)[0].upper()
            number = int(list(pos)[1])
        except:
            print("\nError! Enter the position correctly!\n")
            continue
        orientation = input("Place ship vertically or horizontally? (v/h) ").lower()
        if orientation != "v" and orientation != "vertical" and orientation != "h" and orientation != "horizontal":
            print("\nError! Enter a correct orientation!!\n")
            continue
        if place_ship(p2_grid, p2_ship_lengths, length, letter, number, orientation):
            print("Ship " + str(i + 1) + " placed.")
            print_board(p2_grid, "red")
            break
print("All player 2 ships placed.")
turn = 0;
while True:

    if turn % 2 == 0:
        try:
            pos = input("Player 1's turn:\nEnter position to attack (eg B3): ")
            letter = list(pos)[0].upper()
            number = int(list(pos)[1])
            row = ord(letter) - 65  # Convert position letter to row number
            col = number - 1  # Convert position number to column number
        except:
            print("\nError! Enter the position correctly!\n")
            continue
        if row <= 10 and row >= 0 and col <= 10 and col >= 0:
            p1_attack = attack(p2_grid, p1_opponent_grid, letter, number)
            if p1_attack == "hit":
                print("You hit the opponent's ship!")
                turn += 1
            elif p1_attack == "miss":
                print("You missed the opponent's ship!")
                turn += 1
            elif p1_attack == "alreadyattacked":
                print("You already attacked that position! Try again!")
                continue
            print_board(p1_opponent_grid, "blue")
            if check_win(p1_opponent_grid):
                print("Player one wins!")
                break
        else:
            print(colored("\nError! Enter a valid position!\n", "red"))
            continue
    elif turn % 2 == 1:
        try:
            pos = input("Player 2's turn:\nEnter position to attack (eg B3): ")
            letter = list(pos)[0].upper()
            number = int(list(pos)[1])
            row = ord(letter) - 65  # Convert position letter to row number
            col = number - 1  # Convert position number to column number
        except:
            print("\nError! Enter the position correctly!\n")
            continue
        if row <= 10 and row >= 0 and col <= 10 and col >= 0:
            p2_attack = attack(p1_grid, p2_opponent_grid, letter, number)
            if p2_attack == "hit":
                print("You hit the opponent's ship!")
                turn += 1
            elif p2_attack == "miss":
                print("You missed the opponent's ship!")
                turn += 1
            elif p2_attack == "alreadyattacked":
                print("You already attacked that position! Try again!")
                continue
            print_board(p2_opponent_grid, "red")
            if check_win(p2_opponent_grid):
                print("Player two wins!")
                break
        else:
            print(colored("\nError! Enter a valid position!\n", "red"))
            continue
