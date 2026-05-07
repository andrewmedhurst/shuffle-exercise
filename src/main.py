
from src.consts.consts import STANDARD_DECK
from src.models.card import Card
import random


def shuffle_cards(card_list: list[Card] = STANDARD_DECK) -> list[Card]:
  # Implement the shuffling algorithm here
  if card_list is None:
      return []
  
  deck_length = len(card_list)
  for i in range(deck_length - 1, 0, -1):
     swap_index = random.randint(0, i)
     if swap_index != i:
      card_list[i], card_list[swap_index] = card_list[swap_index], card_list[i]
  return card_list

def main():
  # Create a custom list of cards to shuffle by uncommenting the `card_list` below, modifying the list of cards as needed,
  # and passing it in as an argument to the shuffle_cards function call on line 20. Otherwise, the full standard deck will be shuffled.
  # card_list = [Card("Hearts", "Ace"), Card("Spades", "King"), Card("Diamonds", "Queen")]
  print(f"\nThe Card list before shuffling: \n{STANDARD_DECK}\n")
  shuffled_list = shuffle_cards() # pass in card_list as an argument here if you want to shuffle a custom list of cards instead of the full standard deck
  print(f"The Card list after shuffling: \n{shuffled_list}")

if __name__ == "__main__":
    main()