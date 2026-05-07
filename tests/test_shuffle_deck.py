import unittest
from src.consts.consts import STANDARD_DECK
from src.main import shuffle_cards

class TestShuffleCards(unittest.TestCase):
    def test_shuffle_cards(self):
        # Test that the shuffle_cards function returns a list of the same length as the input
        original_deck = STANDARD_DECK
        shuffled_deck = shuffle_cards(original_deck.copy())
        self.assertEqual(len(original_deck), len(shuffled_deck))

        # Test that the shuffle_cards function returns a list with the same elements as the input
        self.assertCountEqual(original_deck, shuffled_deck)

        # Test that the shuffle_cards function actually shuffles the list
        # There is a very small chance that the shuffled deck is in the same order as the original deck, which may cause this test to fail occasionally.
        self.assertNotEqual(original_deck, shuffled_deck)
    def test_no_two_shuffles_are_the_same(self):
        # Test that two consecutive calls to shuffle_cards do not return the same order (this is a probabilistic test and may fail occasionally)
        original_deck = STANDARD_DECK
        shuffled_deck_1 = shuffle_cards(original_deck.copy())
        shuffled_deck_2 = shuffle_cards(original_deck.copy())
        self.assertNotEqual(shuffled_deck_1, shuffled_deck_2)
    def test_shuffle_none_deck(self):
        shuffled_empty_deck = shuffle_cards(None)
        self.assertEqual([], shuffled_empty_deck)
    def test_shuffle_single_card(self):
        single_card_deck = [STANDARD_DECK[0]]
        shuffled_single_card_deck = shuffle_cards(single_card_deck.copy())
        self.assertEqual(single_card_deck, shuffled_single_card_deck)
    def test_shuffle_custom_deck(self):
        custom_deck = [STANDARD_DECK[0], STANDARD_DECK[1], STANDARD_DECK[2], STANDARD_DECK[3], STANDARD_DECK[4]]
        shuffled_custom_deck = shuffle_cards(custom_deck.copy())
        self.assertEqual(len(custom_deck), len(shuffled_custom_deck))
        self.assertCountEqual(custom_deck, shuffled_custom_deck)
        self.assertNotEqual(custom_deck, shuffled_custom_deck)
    def test_empty_deck(self):
        empty_deck = []
        shuffled_empty_deck = shuffle_cards(empty_deck.copy())
        self.assertEqual(empty_deck, shuffled_empty_deck)