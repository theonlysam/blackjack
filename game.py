from random import shuffle


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def check_card_value(self, card):
        ACE = [1]
        ROYALTY = [11, 12, 13]
        rank = card.rank

        if rank in ROYALTY:
            return 10
        elif rank in ACE:
            return (1, 11)
        else:
            return rank

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

        self.cards = self.shuffle_deck(self.cards)

    def shuffle_deck(self, cards):
        return shuffle(cards)

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
        return [card.__str__() for card in self.cards]

    def show_first_card(self):
        return self.cards[0]

    def show_hand_value(self):
        rank = 0
        hand_value = 0
        for card in self.cards:
            rank = card.check_card_value(card)
            if type(rank) is tuple:
                rank = 1
            else:
                rank = card.rank
            hand_value += rank
        return hand_value

        # return sum([ card.check_card_value(card) for card in self.cards])

    def is_blackjack(self):
        if self.show_hand_value() == 21:
            return True
        else:
            return False

    def is_bust(self):
        if self.show_hand_value() > 21:
            return True
        else:
            return False


class Player:
    def __init__(self):
        self.hand = Hand()

    def request_hit(self, card):
        self.hand.add_card(card)

    def stand(self):
        pass


class Dealer(Player):
    def __init__(self):
        Player.__init__(self)


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
    game.play_round()
