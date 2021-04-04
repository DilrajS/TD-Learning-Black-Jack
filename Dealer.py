class Dealer:

    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def update_score(self, value):
        self.score += value

    def bust(self):
        self.score = 0
