from card import Card

class Hand:
    def __init__(self):
        self.cards : list[Card] = []
        self.hiddenCard : Card = None

    def add_card(self, card, hidden=False):
        if hidden:
            self.hiddenCard = card
        else:
            self.cards.append(card)

    def get_cards(self):
        return self.cards

    def get_hand_points(self, showHidden=False) -> int:
        cards = self.get_cards()
        points = 0
        for card in cards:
            points += card.get_points()
        if self.hiddenCard and showHidden:
            points += self.hiddenCard.get_points()
        return points

    def reveal_hidden_card(self):
        if self.hiddenCard:
            self.cards.append(self.hiddenCard)
            self.hiddenCard = None

    def reset_hand(self):
        self.cards = []
        self.hiddenCard = None


    def __str__(self):
        shownCards = "\n".join([card.show() for card in self.cards])
        if self.hiddenCard:
            shownCards += "\nHidden Card"
        return shownCards

    def __repr__(self):
        return " ".join([card.show() for card in self.cards])
