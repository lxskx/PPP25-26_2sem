def create_map():
    return [
        list("#########"),
        list("#S  #   #"),
        list("# # # # #"),
        list("# #   #E#"),
        list("# ##### #"),
        list("#       #"),
        list("#########")
    ]


def find_player(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "S":
                return row, col


def print_map(maze, player_pos):
    for row in range(len(maze)):
        line = ""
        for col in range(len(maze[row])):
            if (row, col) == player_pos:
                line += "P"
            else:
                cell = maze[row][col]
                line += " " if cell == "S" else cell
        print(line)


def get_new_position(position, command):
    row, col = position

    if command == "w":
        return row - 1, col
    if command == "s":
        return row + 1, col
    if command == "a":
        return row, col - 1
    if command == "d":
        return row, col + 1

    return row, col


def is_valid_move(maze, position):
    row, col = position

    if row < 0 or row >= len(maze):
        return False

    if col < 0 or col >= len(maze[row]):
        return False

    if maze[row][col] == "#":
        return False

    return True


def play_game():
    maze = create_map()
    player_pos = find_player(maze)

    print("Игра: Лабиринт")
    print("Команды: w — вверх, a — влево, s — вниз, d — вправо")
    print("restart — начать заново, exit — выйти")

    while True:
        print()
        print_map(maze, player_pos)

        command = input("\nВаш ход: ").strip().lower()

        if command == "exit":
            print("Выход из игры.")
            return False

        if command == "restart":
            print("Игра начата заново.")
            return True

        if command not in ["w", "a", "s", "d"]:
            print("Ошибка: используйте w, a, s, d, restart или exit.")
            continue

        new_pos = get_new_position(player_pos, command)

        if not is_valid_move(maze, new_pos):
            print("Нельзя туда идти: стена или граница карты.")
            continue

        player_pos = new_pos
        row, col = player_pos

        if maze[row][col] == "E":
            print()
            print_map(maze, player_pos)
            print("Вы нашли выход!")
            break

    while True:
        answer = input("Начать заново? yes/no: ").strip().lower()

        if answer == "yes":
            return True
        elif answer == "no":
            print("Игра завершена.")
            return False
        else:
            print("Ошибка: введите yes или no.")


def main():
    while True:
        restart = play_game()

        if not restart:
            break


main()
