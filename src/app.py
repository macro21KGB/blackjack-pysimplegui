from deck import Deck
from hand import Hand
from gamesystem import GameSystem
from PySimpleGUI import Text, Output, Button, Window, theme, VSep, Menu, WIN_CLOSED



if __name__ == "__main__":

    theme('DarkBlue3')
    menu_def = [["Game", ["Start/Reset", "Exit"]]]


    layout = [
        [Menu(menu_def)],
        [Text("Welcome to Blackjack!")],
        [Text("Dealer:"), VSep(), Text("", key="dealer_total")],
        [Output(key="dealer", size=(30, 10))],
        [Text("Player:")],
        [Output(key="player", size=(30, 10))],
        [Button("Hit", disabled=True), Button("Stand",disabled=True), VSep(), Text("Total: ", key="player_total")],
    ]

    window = Window("Blackjack", layout)


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
        gm.set_window(window)
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
        if event == WIN_CLOSED or event == 'Exit':
            break
        gm.check_game_over()

