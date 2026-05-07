from src.models.card import Card

CARD_SUITES = ["Hearts", "Diamonds", "Clubs", "Spades"]
CARD_RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# Construction of standard deck is technically constant but it is more readable to construct it here rather than hardcoding the list of 52 cards
STANDARD_DECK: list[Card] = [ Card(suit, rank) for suit in CARD_SUITES for rank in CARD_RANKS ]