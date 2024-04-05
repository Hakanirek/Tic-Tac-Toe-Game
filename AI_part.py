import random


class AI:
    def __init__(self, selected_side, grid_list, winning_the_game_comb):
        self.Selected_SIDE = selected_side
        self.grid_list = grid_list
        self.winning_the_game_comb = winning_the_game_comb

    def starting(self):

        if self.Selected_SIDE.lower() == "x":  # burada kullanıcı X olacak bilgisayar 0
            new_list = [i for i in self.grid_list if i != self.grid_list[self.grid_list.index("X")]]  # burada kullanıcın seçmiş olduğu indexi bulduğu ve AI bunun dışında bir random seçim yapacaktır.
            Selected_point = int(random.choice(new_list))

            self.grid_list[Selected_point] = "0"
            print()
        else:

            Selected_point = int(random.choice(self.grid_list))
            self.grid_list[Selected_point] = "X"
