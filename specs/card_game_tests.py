import unittest
from src.card import Card
from src.card_game import *


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("H", 10)
        self.card2 = Card("D", 4)
        self.card3 = Card("H", 1)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace_no_ace(self):
        res = check_for_ace(self.card1)
        self.assertEqual(res, False)

    def test_check_for_ace(self):
        res = check_for_ace(self.card3)
        self.assertEqual(res, True)

    def test_check_highest_card(self):
        res = highest_card(self.card1, self.card2)
        self.assertEqual(res, self.card1)

    def test_check_total(self):
        res = cards_total(self.cards)
        self.assertEqual(15, res)
