class Card:

    def __int__(self, name, count, value):
        self.name = name
        self.count = count
        self.value = value

    def get_name(self):
        return self.name

    def get_count(self):
        return self.count

    def get_value(self):
        return self.value
