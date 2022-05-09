from card import Card
import random


class Deck:
    def __init__(self):
        self.__generate_deck() 
        self.shuffle()       

    def __generate_deck(self):
        """Generate a deck of cards"""
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.deck : list[Card] = []
        for suit in suits:
            for value, point in zip(values, points):
                self.deck.append(Card(suit, value, point))

    def shuffle(self) -> None:
        """Shuffle the deck"""
        self.__generate_deck()
        random.shuffle(self.deck)

    def deal(self) -> Card:
        """Deal a card from the deck"""
        return self.deck.pop()
