from deck import Deck
from hand import Hand
import PySimpleGUI as sg


sg.theme('DarkBlue14')


class GameSystem:
    def __init__(self, player: Hand, dealer: Hand, deck: Deck):
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.game_over = False

    def update_player(self):
        """Update the player interface"""
        window["player"].update(self.player)
        window["player_total"].update("Total: " + str(self.player.get_hand_points())) 


    def update_score(self):
        """Update the score"""
        window["player_total"].update("Total: " + str(self.player.get_hand_points()))
        if self.game_over:
            window["dealer_total"].update("Total: " + str(self.dealer.get_hand_points()))

    def reset_and_deal(self):
        """Reset the game and deal a new hand, also shuffle the deck"""
        self.game_over = False
        window["Hit"].update(disabled=False)
        window["Stand"].update(disabled=False)
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck.shuffle()
        self.deal_starting_hand()
        window["dealer_total"].update("Total: " + str(self.dealer.get_hand_points()))

    def deal_starting_hand(self):
        self.dealer.add_card(self.deck.deal(), True)
        self.player.add_card(self.deck.deal(), False)
        self.dealer.add_card(self.deck.deal(), False)
        self.player.add_card(self.deck.deal(), False)

    def check_hit(self):
        """Check if the player has lose"""
        if self.player.get_hand_points() > 21:
            self.game_over = True
            sg.Popup("Player loses!\nDealer wins!")
            self.update_score()
        if self.player.get_hand_points() == 21 and self.dealer.get_hand_points() != 21:
            self.game_over = True
            sg.Popup("Player wins!\nDealer loses!")
            self.update_score()
        if self.player.get_hand_points() == 21 and self.dealer.get_hand_points() == 21:
            self.game_over = True
            sg.Popup("Player loses!\nDealer wins!")
        
    def check_game_over(self):
        """Check if the game is over"""
        if self.game_over:
            window["Hit"].update(disabled=True)
            window["Stand"].update(disabled=True)
            self.dealer.reveal_hidden_card()
            window["dealer"].update(self.dealer)
            self.update_score()

    def check_stand(self):
        """Check if the player has stand"""
        if self.player.get_hand_points() == 21 and self.dealer.get_hand_points() == 21:
            self.game_over = True
            sg.Popup("Player loses!\nDealer wins!")
            self.update_score()
        if self.player.get_hand_points() > self.dealer.get_hand_points() and self.player.get_hand_points() <= 21:
            self.game_over = True
            sg.Popup("Player wins!\nDealer loses!")
            self.update_score()
        if self.player.get_hand_points() < self.dealer.get_hand_points() and self.dealer.get_hand_points() <= 21:
            self.game_over = True
            sg.Popup("Player loses!\nDealer wins!")
            self.update_score()


menu_def = [["Game", ["Start/Reset", "Exit"]]]


layout = [
    [sg.Menu(menu_def)],
    [sg.Text("Welcome to Blackjack!")],
    [sg.Text("Dealer:"), sg.VSep(), sg.Text("", key="dealer_total")],
    [sg.Output(key="dealer", size=(30, 10))],
    [sg.Text("Player:")],
    [sg.Output(key="player", size=(30, 10))],
    [sg.Button("Hit", disabled=True), sg.Button("Stand",disabled=True), sg.VSep(), sg.Text("Total: ", key="player_total")],
]

window = sg.Window("Blackjack", layout)


player = Hand()
dealer = Hand() 
deck = Deck()
gm = GameSystem(player, dealer, deck)

def check_menu_event(event):
    if event == "Start/Reset":
        gm.reset_and_deal()
        window["dealer"].update(dealer)
        gm.update_player()
    if event == "Exit":
        window.close()

while True:
    event, values = window.Read()
    check_menu_event(event)
    if event == "Hit":
        player.add_card(deck.deal())
        gm.update_player()
        gm.check_hit()
    if event == "Stand":
        gm.update_player()
        dealer.reveal_hidden_card()
        window["dealer"].update(dealer)
        window["dealer_total"].update("Total: " + str(dealer.get_hand_points(True)))
        gm.check_stand()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    gm.check_game_over()

