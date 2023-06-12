from random import shuffle


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def check_card_value(self):
        if self.rank in (11, 12, 13):
            return 10
        elif self.rank == 1:
            return (1, 11)
        else:
            return self.rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"


class Deck:

    CARD_SUITS = ["♠️", "♣️", "♥️", "♦️"]

    def __init__(self):
        self.cards = [
            Card(rank, suit) for suit in self.CARD_SUITS for rank in range(1, 14)
        ]
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)

    def __str__(self):
        return f"{[str(card) for card in self.cards]}"


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def show_cards(
        self,
    ):  # from a testing perspective should I use the class attribute or paramter
        return [str(card) for card in self.cards]

    def show_first_card(self):
        return self.cards[0]

    def show_hand_value(self):
        rank = 0
        hand_value = 0
        for card in self.cards:
            rank = card.check_card_value()
            if type(rank) is tuple:
                rank = 1
            else:
                rank = card.rank
            hand_value += rank
        return hand_value

        # return sum([ card.check_card_value() for card in self.cards])

    def is_blackjack(self):
        return self.show_hand_value() == 21

    def is_bust(self):
        return self.show_hand_value() > 21


class Player:
    def __init__(self):
        self.hand = Hand()

    def request_hit(self, card):
        self.hand.add_card(card)

    def stand(self):
        pass


class Dealer(Player):
    def __init__(self):
        super().__init__(self)


class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

    def play_round(self):
        deck = Deck()
        card = deck.deal_card()
        self.player.request_hit(card)

    def check_winner(self):
        if self.player.hand.is_blackjack:
            pass

    def check_winner(self):
        pass

    def reset(self):
        pass


if __name__ == "__main__":
    game = Game()
    # TODO: play several rounds till blackjack / bust
    game.play_round()
