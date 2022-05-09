from hand import Hand
from deck import Deck
from PySimpleGUI import Popup

class GameSystem:
    def __init__(self, player: Hand, dealer: Hand, deck: Deck):
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.window = None
        self.game_over = False

    def update_player(self):
        """Update the player interface"""
        self.window["player"].update(self.player)
        self.window["player_total"].update("Total: " + str(self.player.get_hand_points())) 

    def set_window(self, window):
        self.window = window

    def update_score(self):
        """Update the score"""
        self.window["player_total"].update("Total: " + str(self.player.get_hand_points()))
        if self.game_over:
            self.window["dealer_total"].update("Total: " + str(self.dealer.get_hand_points()))

    def reset_and_deal(self):
        """Reset the game and deal a new hand, also shuffle the deck"""
        self.game_over = False
        self.window["Hit"].update(disabled=False)
        self.window["Stand"].update(disabled=False)
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck.shuffle()
        self.deal_starting_hand()
        self.window["dealer_total"].update("Total: " + str(self.dealer.get_hand_points()))

    def deal_starting_hand(self):
        self.dealer.add_card(self.deck.deal(), True)
        self.player.add_card(self.deck.deal(), False)
        self.dealer.add_card(self.deck.deal(), False)
        self.player.add_card(self.deck.deal(), False)

    def check_hit(self):
        """Check if the player has lose"""
        if self.player.get_hand_points() > 21:
            self.game_over = True
            Popup("Player loses!\nDealer wins!")
            self.update_score()
        if self.player.get_hand_points() == 21 and self.dealer.get_hand_points() != 21:
            self.game_over = True
            Popup("Player wins!\nDealer loses!")
            self.update_score()
        if self.player.get_hand_points() == 21 and self.dealer.get_hand_points() == 21:
            self.game_over = True
            Popup("Player loses!\nDealer wins!")
        
    def check_game_over(self):
        """Check if the game is over"""
        if self.game_over:
            self.window["Hit"].update(disabled=True)
            self.window["Stand"].update(disabled=True)
            self.dealer.reveal_hidden_card()
            self.window["dealer"].update(self.dealer)
            self.update_score()

    def check_stand(self):
        """Check if the player has stand"""
        if self.player.get_hand_points() == 21 and self.dealer.get_hand_points() == 21:
            self.game_over = True
            Popup("Player loses!\nDealer wins!")
            self.update_score()
        if self.player.get_hand_points() > self.dealer.get_hand_points() and self.player.get_hand_points() <= 21:
            self.game_over = True
            Popup("Player wins!\nDealer loses!")
            self.update_score()
        if self.player.get_hand_points() < self.dealer.get_hand_points() and self.dealer.get_hand_points() <= 21:
            self.game_over = True
            Popup("Player loses!\nDealer wins!")
            self.update_score()
