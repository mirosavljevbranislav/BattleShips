import random

board = [["•" for _ in range(7)] for _ in range(14)]
hidden_board = [["•" for _ in range(7)] for _ in range(7)]


def print_board():
    print("\t0\t 1\t  2\t   3\t4\t 5\t  6\t")
    for i in range(len(board)):
        print(f"{i}", board[i], "\n")
        if i == len(board) / 2 - 1:
            print("===================================")


def print_hidden_board():
    print("\t0\t 1\t  2\t   3\t4\t 5\t  6\t")
    for i in range(len(hidden_board)):
        print(f"{i}", hidden_board[i], "\n")
    print("===================================")
    for j in range(int(len(board) / 2), len(board)):
        print(f"{j}", board[j], "\n")


ship_types = {"large": 4,
              "medium": 3,
              "small": 2,
              "smallest": 1}


def check_first_half():
    x_counter = 0
    for i in range(int(len(board) / 2)):
        for j in board[i]:
            if j == "X":
                x_counter += 1
    return x_counter


def check_second_half():
    second_x_counter = 0
    for k in range(int(len(board) / 2), len(board)):
        for h in board[k]:
            if h == "X":
                second_x_counter += 1
    return second_x_counter


def check_ship_spawn(ship_length: int, h_or_v: str, x_coordinate: int, y_coordinate: int):
    """
    Checks if ship can spawn horizontally or vertically depending on spawn point and length of ship
    :param ship_length: length of ship in tiles
    :param h_or_v: horizontal or vertical
    :param x_coordinate: x spawn coordinate
    :param y_coordinate: y spawn coordinate
    :return: True or False denepding if it can spawn or not
    """

    if h_or_v == "horizontal":
        for j in range(ship_length):
            if board[y_coordinate][x_coordinate + j] == "•" and board[y_coordinate][x_coordinate + j] != "X" or \
                    board[y_coordinate][x_coordinate - j] == "•" and board[y_coordinate][x_coordinate - j] != "X":
                return True
            else:
                return False
    elif h_or_v == "vertical":
        for k in range(ship_length):
            if board[y_coordinate + k][x_coordinate] == "•" and board[y_coordinate + k][x_coordinate] != "X" or \
                    board[y_coordinate - k][x_coordinate] == "•" and board[y_coordinate - k][x_coordinate] != "X":
                return True
            else:
                return False


def generate_ship(ship_type: str, x_coordinates: int, y_coordinates: int):
    """
    Generates ship, this method is called in generate_ships method, it generates single ship based on size that is required
    :param ship_type: this is ship size: large, medium, small, smallest
    :param x_coordinates: x spawn coordinates
    :param y_coordinates: y spawn coordinates
    :return: None
    """
    ship_size = ship_types[ship_type]

    h_or_v = random.randint(1, 2)
    if h_or_v == 1:
        if y_coordinates - ship_size >= 0:
            while ship_size >= 0:
                if check_ship_spawn(ship_length=ship_size,
                                    h_or_v="vertical",
                                    x_coordinate=x_coordinates,
                                    y_coordinate=y_coordinates):
                    board[y_coordinates][x_coordinates] = "X"
                    y_coordinates -= 1
                    ship_size -= 1
                else:
                    break
        elif y_coordinates + ship_size <= len(board) / 2:
            while ship_size >= 0:
                if check_ship_spawn(ship_length=ship_size,
                                    h_or_v="vertical",
                                    x_coordinate=x_coordinates,
                                    y_coordinate=y_coordinates):
                    board[y_coordinates][x_coordinates] = "X"
                    y_coordinates += 1
                    ship_size -= 1
                else:
                    break
    elif h_or_v == 2:
        if x_coordinates - ship_size >= 0:
            while ship_size >= 0:
                if check_ship_spawn(ship_length=ship_size,
                                    h_or_v="horizontal",
                                    x_coordinate=x_coordinates,
                                    y_coordinate=y_coordinates):
                    board[y_coordinates][x_coordinates] = "X"
                    x_coordinates -= 1
                    ship_size -= 1
                else:
                    break
        elif x_coordinates + ship_size <= 6:
            while ship_size >= 0:
                if check_ship_spawn(ship_length=ship_size,
                                    h_or_v="horizontal",
                                    x_coordinate=x_coordinates,
                                    y_coordinate=y_coordinates):
                    board[y_coordinates][x_coordinates] = "X"
                    x_coordinates += 1
                    ship_size -= 1
                else:
                    break


def generate_ships():
    """
    Method that generates ships for bot and player, it uses while loop instead of for cause it loops twice from 0-10
    generating 1 large ship, 2 medium ships, 3 small ships, and 4 smallest ships, based on value of i
    :return: None
    """
    bot_generating_phase = True
    player_generating_phase = False
    i = 1
    while i <= 10:

        if i == 1:
            while bot_generating_phase:
                random_x_coordinate = random.randint(0, 6)
                random_y_coordinate = random.randint(0, 6)
                if board[random_y_coordinate][random_x_coordinate] == "•":
                    generate_ship(ship_type="large",
                                  x_coordinates=random_x_coordinate,
                                  y_coordinates=random_y_coordinate)

                    break
            if player_generating_phase:
                while player_generating_phase:
                    random_x_coordinate = random.randint(0, 6)
                    random_y_coordinate = random.randint(7, 13)
                    if board[random_y_coordinate][random_x_coordinate] == "•":
                        generate_ship(ship_type="large",
                                      x_coordinates=random_x_coordinate,
                                      y_coordinates=random_y_coordinate)

                        break
            i += 1
        elif i == 2 or i == 3:
            while bot_generating_phase:
                random_x_coordinate = random.randint(0, 6)
                random_y_coordinate = random.randint(0, 6)
                if board[random_y_coordinate][random_x_coordinate] == "•":
                    generate_ship(ship_type="medium",
                                  x_coordinates=random_x_coordinate,
                                  y_coordinates=random_y_coordinate)
                    break
            if player_generating_phase:
                while player_generating_phase:
                    random_x_coordinate = random.randint(0, 6)
                    random_y_coordinate = random.randint(7, 13)
                    if board[random_y_coordinate][random_x_coordinate] == "•":
                        generate_ship(ship_type="medium",
                                      x_coordinates=random_x_coordinate,
                                      y_coordinates=random_y_coordinate)

                        break
            i += 1
        elif i == 4 or i == 5 or i == 6:
            while bot_generating_phase:
                random_x_coordinate = random.randint(0, 6)
                random_y_coordinate = random.randint(0, 6)
                if board[random_y_coordinate][random_x_coordinate] == "•":
                    generate_ship(ship_type="small",
                                  x_coordinates=random_x_coordinate,
                                  y_coordinates=random_y_coordinate)
                    break
            if player_generating_phase:
                while player_generating_phase:
                    random_x_coordinate = random.randint(0, 6)
                    random_y_coordinate = random.randint(7, 13)
                    if board[random_y_coordinate][random_x_coordinate] == "•":
                        generate_ship(ship_type="small",
                                      x_coordinates=random_x_coordinate,
                                      y_coordinates=random_y_coordinate)

                        break
            i += 1
        elif i == 7 or i == 8 or i == 9 or i == 10:
            while bot_generating_phase:
                random_x_coordinate = random.randint(0, 6)
                random_y_coordinate = random.randint(0, 6)
                if board[random_y_coordinate][random_x_coordinate] == "•":
                    generate_ship(ship_type="smallest",
                                  x_coordinates=random_x_coordinate,
                                  y_coordinates=random_y_coordinate)
                    if i == 10:
                        bot_generating_phase = False
                        player_generating_phase = True
                        i = 0
                    break
            if player_generating_phase:
                while player_generating_phase:
                    random_x_coordinate = random.randint(0, 6)
                    random_y_coordinate = random.randint(7, 13)
                    if board[random_y_coordinate][random_x_coordinate] == "•":
                        generate_ship(ship_type="smallest",
                                      x_coordinates=random_x_coordinate,
                                      y_coordinates=random_y_coordinate)

                        break
            i += 1


def check_ship_surroundings(ship_y_coordinate: int, ship_x_coordinate: int):
    """
    This method checks if there are ship parts nearby of ship that has been hit
    :param ship_y_coordinate: y coordinate of bot's shot
    :param ship_x_coordinate: x coordinate of bot's shot
    :return: x and y coordinates of nearby ship part
    """
    founded_x_coordinates = 0
    founded_y_coordinates = 0
    if ship_y_coordinate - 1 >= 6 and board[ship_y_coordinate - 1][ship_x_coordinate] == "X":
        founded_y_coordinates = ship_y_coordinate - 1
        founded_x_coordinates = ship_x_coordinate
    elif ship_y_coordinate + 1 <= 13 and board[ship_y_coordinate + 1][ship_x_coordinate] == "X":
        founded_y_coordinates = ship_y_coordinate + 1
        founded_x_coordinates = ship_x_coordinate
    elif ship_x_coordinate - 1 >= 0 and board[ship_y_coordinate][ship_x_coordinate - 1] == "X":
        founded_y_coordinates = ship_y_coordinate
        founded_x_coordinates = ship_x_coordinate - 1
    elif ship_x_coordinate + 1 <= 6 and board[ship_y_coordinate][ship_x_coordinate + 1] == "X":
        founded_y_coordinates = ship_y_coordinate
        founded_x_coordinates = ship_x_coordinate + 1
    return founded_y_coordinates, founded_x_coordinates


def game():
    """
    Main function, it has while loop that loops until game is finished, player can choose coordinates where to shoot, if
    it was a hit it continues player turn loop, if it wasn't then bot randomly shots, if he hits once, method
    check_ship_surroundings is called to see if he can hit something else that is nearby, so bot can play a little smarter,
    there is 1 in 4 chance that he will hit something near him.
    :return: None
    """
    game_end = False
    player_turn = True
    another_bot_hit = False
    last_x_hit = 0
    last_y_hit = 0
    while not game_end:
        while player_turn:
            player_y_choice = int(input("Where do you want to shoot 0 - 6? Y coordinates = ?"))
            player_x_choice = int(input("Where do you want to shoot 0 - 6? X coordinates = ?"))
            if player_x_choice not in range(6) and player_y_choice not in range(6):
                print("Oops, out of range, try again!")
                continue
            else:
                print(f"You shot at coordinates: X: {player_x_choice}, Y: {player_y_choice}")
                if board[player_y_choice][player_x_choice] == "X":
                    print("And it was a hit! Nice!")
                    board[player_y_choice][player_x_choice] = "💀"
                    hidden_board[player_y_choice][player_x_choice] = "💀"
                    print_hidden_board()
                    continue

                else:
                    print("But you missed...")
                    board[player_y_choice][player_x_choice] = "❌"
                    hidden_board[player_y_choice][player_x_choice] = "❌"
                    print_hidden_board()
                    player_turn = False

        while not player_turn:
            while another_bot_hit:
                tile_choice = random.randint(1, 4)
                y_coordinates, x_coordinates = check_ship_surroundings(last_y_hit, last_x_hit)
                if tile_choice == 2:
                    print(f"Bot hit! Coordinates: X:{x_coordinates} Y: {y_coordinates}")
                    board[y_coordinates][x_coordinates] = "💀"
                    print_hidden_board()
                else:
                    print("Bot missed his second shot...")
                    board[y_coordinates][x_coordinates] = "❌"
                    print_hidden_board()
                    another_bot_hit = False
                    player_turn = True

            bot_x_choice = random.randint(0, 6)
            bot_y_choice = random.randint(7, 13)
            last_x_hit = bot_x_choice
            last_y_hit = bot_y_choice
            if [bot_y_choice, bot_x_choice] not in used_bot_choices:
                print(f"Bot shot at coordinates: X: {bot_x_choice}, Y: {bot_y_choice}")
                if board[bot_y_choice][bot_x_choice] == "X":
                    print("Bot scored a shot!")
                    used_bot_choices.append([bot_y_choice, bot_x_choice])
                    board[bot_y_choice][bot_x_choice] = "💀"
                    another_bot_hit = True
                    print_hidden_board()
                else:
                    print("Bot missed..")
                    used_bot_choices.append([bot_y_choice, bot_x_choice])
                    board[bot_y_choice][bot_x_choice] = "❌"
                    print_hidden_board()
                    another_bot_hit = False
                    player_turn = True
        if check_first_half() == 0 or check_second_half() == 0:
            print("END")
            game_end = True


used_bot_choices = []


if __name__ == '__main__':
    while True:
        generate_ships()
        if check_first_half() == 20 and check_second_half() == 20:
            break
        else:
            board = [["•" for _ in range(7)] for _ in range(14)]
    print_hidden_board()
    game()
