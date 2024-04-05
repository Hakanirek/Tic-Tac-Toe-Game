from AI_part import AI

grid_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

Selected_SIDE = "0"

winning_the_game_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],
                         [0, 4, 8], [2, 4, 6]]



def winning_the_game():
    for comb in winning_the_game_comb:
        if grid_list[comb[0]] == "X" and grid_list[comb[1]] == "X" and grid_list[comb[2]] == "X":
            print("Player X won :)))")
            return False
        elif grid_list[comb[0]] == "0" and grid_list[comb[1]] == "0" and grid_list[comb[2]] == "0":
            print("Player 0 won :)))")
            return False
    return True


def show_grid(grid_list):
    print(f"""
          {grid_list[0]} | {grid_list[1]} | {grid_list[2]}\n
          ___ ___ ___\n
          {grid_list[3]} | {grid_list[4]} | {grid_list[5]}\n
          ___ ___ ___\n
          {grid_list[6]} | {grid_list[7]} | {grid_list[8]}\n
""")


def two_player_game():
    is_continue = True
    global Selected_SIDE
    global grid_list
    show_grid(grid_list)
    while is_continue:

        if Selected_SIDE.lower() == "x":
            print("PLAYER X >>>>")
            selected_input_x = int(input("Select a number from the grid (0,8): "))
            if 0 <= selected_input_x <= 8:

                if grid_list[selected_input_x] != "X" and grid_list[selected_input_x] != "0":
                    grid_list[selected_input_x] = "X"
                    show_grid(grid_list)

                else:
                    print("This area is used before. please try again...")
                    show_grid(grid_list)
                    continue

            else:
                print("Invalid Input. please try again...")
                show_grid(grid_list)
                continue
        else:
            print("PLAYER 0 >>>>")
            selected_input_o = int(input("Select a number from the grid (0,8): "))
            if 0 <= selected_input_o <= 8:

                if grid_list[selected_input_o] != "X" and grid_list[selected_input_o] != "0":
                    grid_list[selected_input_o] = "0"
                    show_grid(grid_list)
                else:
                    print("This area is used before. please try again...")
                    show_grid(grid_list)
                    continue

            else:
                print("Invalid Input. please try again...")
                show_grid(grid_list)
                continue

        if Selected_SIDE.lower() == "x":
            Selected_SIDE = "0"

        else:
            Selected_SIDE = "X"

        is_continue = winning_the_game()


def game():
    global grid_list
    global Selected_SIDE

    print("Please Select which game do you want to play:")
    answer = input("1. 2 Player Game\n"
                   "2. Play against computer")

    if answer == "1":

        Selected_SIDE = input("Which side do you want to be? (X or O)")

        if Selected_SIDE.lower() == "x" or Selected_SIDE.lower() == "0":
            two_player_game()

        else:
            print("Invalid input. Try again...")
            game()

        play_again = input("Do you want to play again? (y or n)")

        if play_again == "y":
            grid_list = ["O", "1", "2", "3", "4", "5", "6", "7", "8"]
            game()

    elif answer == "2":
        print("You are playing with AI now.")
        Selected_SIDE = input("Please select the side you want to play (X OR 0):\n")
        print("PLAYER X >>>>")
        selected_input_x = int(input("Select a number from the grid (0,8): "))
        AI_example = AI(selected_side=Selected_SIDE, grid_list=grid_list, winning_the_game_comb=winning_the_game_comb)

        if 0 <= selected_input_x <= 8:

            if grid_list[selected_input_x] != "X" and grid_list[selected_input_x] != "0":
                grid_list[selected_input_x] = "X"
                show_grid(grid_list)

            else:
                print("This area is used before. please try again...")
                show_grid(grid_list)


        else:
            print("Invalid Input. please try again...")
            show_grid(grid_list)

        print("AI")
        AI_example.starting()
        show_grid(grid_list)


game()


print(grid_list)