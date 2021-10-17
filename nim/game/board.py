import random

class Board():
    def __init__(self):
        self._piles = self._prepare()
    
    def _prepare(self):
        piles = []
        num_piles = random.randint(2, 5)
        for _ in range(num_piles):
            num_stones = random.randint(1, 9)
            piles.append(num_stones)
        return piles

    def apply(self, move):
        pile = move.get_pile()
        stones = move.get_stones()
        self._piles[pile] -= stones

    def is_empty(self):
        for stones in self._piles:
            if stones > 0:
                return False
        return True

    def to_string(self):
        rt_string = "--------------------\n"
        for row in range(len(self._piles)):
            rt_string += f"{row}: {'O '*self._piles[row]}\n"
        rt_string += "--------------------"
        return rt_string