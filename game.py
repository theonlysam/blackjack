import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{self.suit}"

    def __repr__(self):
        return f"Card('{self.value}', '{self.suit}')"


class Deck:

    CARD_VALUE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    CARD_SUIT = ["\u2663", "\u2665", "\u2666", "\u2660"]

    def __init__(self):
        self.deck = []
        self.new_deck()

    def new_deck(self):
        for suit in self.CARD_SUIT:
            for value in self.CARD_VALUE:
                self.deck.append(Card(value, suit))
        random.shuffle(self.deck)

    def __str__(self):
        return f"{[str(card) for card in self.deck]}"


class Hand:
    def __init__(self):
        self.cards = []

    # Todo
    # should be able to add cards to the hand
    # should be able to display / show all the cards in the hand and total value


class Player:
    def __init__(self):
        self.hand = Hand()

    # Todo
    # player should be able to request a hit or hold


class Dealer:
    # Todo
    # Dealer should be able to request a hit or hold
    # Dealer should be able to give/issue a card from the deck
    # should be able to display / show all the cards in the hand and total value
    pass


if __name__ == "__main__":
    cards = Deck()
    print(cards)
