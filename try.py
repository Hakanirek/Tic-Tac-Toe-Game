import random
winning_the_game = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 7], [1, 4, 5], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]

grid_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]



a = ["0", "0", "1"]

selected_point = next((value for value in a if value != "0"), None)

print(int(random.choice(grid_list)))