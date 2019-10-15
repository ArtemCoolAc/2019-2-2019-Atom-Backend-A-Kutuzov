import unittest
import game_cross_zero

class MyTestCase(unittest.TestCase):
    def test_mistakes(self):
        self.assertEqual('Error', game_cross_zero.Game.validate_number('0'))
        self.assertEqual('Error', game_cross_zero.Game.validate_number('10'))
        self.assertEqual('Error', game_cross_zero.Game.validate_number('True'))
        self.assertEqual('Error', game_cross_zero.Game.validate_number('False'))
        self.assertEqual('Error', game_cross_zero.Game.validate_number('5,34'))
        self.assertEqual('Error', game_cross_zero.Game.validate_number('3.3'))
        self.assertEqual('Error', game_cross_zero.Game.validate_number('-5'))
        self.assertEqual('Error', game_cross_zero.Game.validate_number('strgrfgtfh'))

    def test_correct_values(self):
        self.assertEqual(5, game_cross_zero.Game.validate_number('5'))
        self.assertEqual(3, game_cross_zero.Game.validate_number('3'))

    def test_incorrect_types(self):
        self.assertEqual('TypeError', game_cross_zero.Game.validate_number(True))
        self.assertEqual('TypeError', game_cross_zero.Game.validate_number(False))
        self.assertEqual('TypeError', game_cross_zero.Game.validate_number([1, 2, 4, 5]))
        self.assertEqual('TypeError', game_cross_zero.Game.validate_number({1: '3', 4: 'dsfsef'}))
        self.assertEqual('TypeError', game_cross_zero.Game.validate_number((1, 3, 5)))
        self.assertEqual('TypeError', game_cross_zero.Game.validate_number([3]))

if __name__ == '__main__':
    unittest.main()
