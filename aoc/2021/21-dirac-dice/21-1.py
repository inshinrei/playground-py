class Dice:
    def __init__(self, sides=100):
        self.sides = sides
        self.value = 0
        self.times_rolled = 0

    def roll(self):
        self.times_rolled += 1
        self.value = self.value % self.sides + 1
        return self.value


with open('./input.txt', encoding='utf-8') as input_data:
    data = input_data.read().splitlines()
    pos1 = int(data[0].split(' ')[-1])
    pos2 = int(data[1].split(' ')[-1])
    score1, score2 = 0, 0
    dice = Dice()
    while True:
        pos1 = (pos1 + dice.roll() + dice.roll() + dice.roll() - 1) % 10 + 1
        score1 += pos1
        if score1 >= 1000:
            exit()
        pos2 = (pos2 + dice.roll() + dice.roll() + dice.roll() - 1) % 10 + 1
        score2 = pos2
        if score2 >= 1000:
            exit()
