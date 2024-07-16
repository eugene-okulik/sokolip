class Flowers:
    def __init__(self, name, color, fresher, live_time, price, length):
        self.name = name
        self.color = color
        self.fresher = fresher
        self.live_time = live_time
        self.price = price
        self.length = length


class Rose(Flowers):
    def __init__(self, name, color, fresher, live_time, price, length, prickle):
        super().__init__(name, color, fresher, live_time, price, length)
        self.prickle = prickle


class Daisy(Flowers):
    def __init__(self, name, color, fresher, live_time, price, length, bush):
        super().__init__(name, color, fresher, live_time, price, length)
        self.bush = bush


class Tulpan(Flowers):
    def __init__(self, name, color, fresher, live_time, price, length):
        super().__init__(name, color, fresher, live_time, price, length)


class Buket():
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)

    def cost(self):
        total_cost = sum(flower.price for flower in self.flowers)
        print(f'Стоимость букета: {total_cost}')

    def live_time_buket(self):
        live_time = sum(flower.live_time for flower in self.flowers) / len(self.flowers)
        print(f'Время жизни букета: {live_time}')

    def sort_flowers_by(self, key='color'):
        if key == 'color':
            self.flowers.sort(key=lambda x: x.color)
            for flower in buket_1.flowers:
                print(flower)
        elif key == 'name':
            self.flowers.sort(key=lambda x: x.name)
            for flower in buket_1.flowers:
                print(flower)
        elif key == 'length':
            self.flowers.sort(key=lambda x: x.length)
            for flower in buket_1.flowers:
                print(flower)
        elif key == 'price':
            self.flowers.sort(key=lambda x: x.price)
            for flower in buket_1.flowers:
                print(flower)


white_rose = Rose('w_rose', 'white', 2, 10, 100, 17, 'yes')
red_rose = Rose('r_rose', 'red', 1, 11, 120, 17, 'no')
blue_rose = Rose('b_rose', 'red', 2, 8, 105, 18, 'yes')
big_daisy = Daisy('b_daisy' 'white', 3, 6, 80, 15, 'no', True)
small_daisy = Daisy('s_daisy', 'pink', 4, 5, 97, 18, 'yes')
red_tulp = Tulpan('r_tulp', 'red', 4, 7, 120, 20)
white_tulp = Tulpan('w_tulp', 'white', 5, 12, 105, 21)
pink_tulp = Tulpan('p_tulp', 'pink', 3, 14, 150, 21)
buket_1 = Buket()
buket_1.add_flowers(white_rose)
buket_1.add_flowers(red_rose)
buket_1.add_flowers(big_daisy)
buket_1.add_flowers(pink_tulp)
buket_1.cost()
buket_1.live_time_buket()
buket_1.sort_flowers_by('price')
