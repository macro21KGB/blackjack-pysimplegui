class Card:
    def __init__(self, suit : list[str], value : list[str], points=10):
        self.suit = suit
        self.value = value
        self.points = points

    def __str__(self):
        return f"{self.value} {self.suit}"

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def show(self):
        return f"{self.value} of {self.suit} ({self.points})"

    def change_points(self, points :int):
        self.points = points

    def get_points(self) -> int:    
        return self.points

