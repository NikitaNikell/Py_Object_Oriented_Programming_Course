class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] # ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.ind = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind >= len(self.cards)-1:
            raise StopIteration
        self.ind += 1
        return f"{self.cards[self.ind].rank} {self.cards[self.ind].suit}"


deck = Deck()
for card in deck:
    print(card)


# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#     def __str__(self):
#         return f"{self.rank} {self.suit}"
#
#
# class Deck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#
#     def __init__(self):
#         self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __iter__(self):
#         return iter(self.cards)
#
#
# deck = Deck()
# for card in deck:
#     print(card)