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


white_rose = Rose('w_rose', 'white', 2, 10, 100, 17, True)
red_rose = Rose('r_rose', 'red', 1, 11, 120, 17, False)
blue_rose  = Rose('b_rose', 'red', 2, 8, 105, 18, True)
big_daisy = Daisy('b_daisy' 'white', 3, 6, 80, 15, False)
small_daisy = Daisy('s_daisy', 'pink', 4, 5, 97, 18, True)
red_tulpan = Tulpan('r_tulpan', 'red', 4, 7, 120, 20)
white_tulpan = Tulpan('w_tulpan', 'white', 5, 12, 105, 21)
pink_tulpan = Tulpan('p_tulpan', 'pink', 3, 14, 150, 21)

class Buket()