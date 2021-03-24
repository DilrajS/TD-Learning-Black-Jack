class Card:

    def __int__(self, name, color, count, value):
        # name of card (A, 2-10, J, Q, K)
        self.name = name
        # 4 different colors: Spades (black), Diamonds (red), Clubs (black) and Hearts (red)
        self.colors = color
        # 4 in a deck of 52
        self.count = count
        # [A = 1 or 10] & [J = Q = K = 10]
        self.value = value

    def get_name(self):
        return self.name

    def get_color(self):
        return self.colors

    def get_count(self):
        return self.count

    def get_value(self):
        return self.value
