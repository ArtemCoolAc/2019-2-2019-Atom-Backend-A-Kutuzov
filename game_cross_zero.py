"""Module just for fun game"""
# -*- coding: utf-8 -*-
from __future__ import print_function
from itertools import chain
import tabulate
import numpy

class Game(object):
    """Класс игры"""
    def __init__(self):
        self.field = numpy.array([(-10, -10, -10), (-10, -10, -10), (-10, -10, -10)])
        self.rendered_field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def render_field(self):
        """Метод отрисовки поля"""
        print(tabulate.tabulate(self.rendered_field, tablefmt='grid'))

    def check_free_place(self, i, j):
        """Метод проверки клетки на занятость"""
        return self.field[i][j] == -10

    def check_win(self):
        """Метод проверки на чью-либо победу"""
        return any(summa % 3 == 0 and \
summa > 0 for summa in list(chain(*[tuple(list((self.field.sum(axis=0)))), \
tuple(list((self.field.sum(axis=1)))), (sum(self.field.diagonal()), \
sum(numpy.fliplr(self.field).diagonal()))])))

    @staticmethod
    def validate_number(number):
        """Метод проверки номера клеточки"""
        if not isinstance(number, str):
            return 'TypeError'
        try:
            value = int(number)
        except ValueError:
            return 'Error'
        except TypeError:
            return 'Error'
        except ZeroDivisionError:
            return 'Error'
        else:
            if (value < 1 or value > 9):
                return 'Error'
        return value

    def game_logic(self):
        """Метод реализации игровой логики"""
        symbols = ('X', 'O')
        move_counter = 0
        start = True
        while not self.check_win() and move_counter != 9 or start:
            start = False
            num_for_validation = input('Введите номер клеточки, куда поставить {}\n' \
.format(symbols[move_counter % 2]))
            number = Game.validate_number(num_for_validation)
            if number == 'Error':
                print('Да введите число от 1 до 9, сложно что ли?')
            else:
                our_index = number - 1  # у нас же индексы от 1 до 9
                index = (our_index // 3, our_index % 3)
                if not self.check_free_place(index[0], index[1]):
                    print('Эта клеточка уже занята, пожалуйста, посмотрите другие варианты')
                else:
                    self.field[index[0]][index[1]] = move_counter % 2 + 1  # 'X' - 1, 'O' - 2
                    self.rendered_field[index[0]][index[1]] = symbols[move_counter % 2]
                    move_counter += 1
                    print('Ситуация на поле боя: (ходов произведено {})'.format(move_counter))
                    self.render_field()
        print('Окончание игры')
        if not self.check_win() and move_counter == 9:
            print('Это ничья. Но это ожидаемый результат')

def main():
    """Метод main()"""
    print("Приветствую вас в игре 'крестики-нолики'")
    answer = True
    while answer:
        current_game = Game()
        current_game.render_field()
        current_game.game_logic()
        answer = None
        while answer is None:
            print("Хотите ли продолжить игровой сеанс? 'y(д)' - да, 'n(н)' - нет")
            str_answer = input().lower()
            answer = True if str_answer == 'y' or str_answer == 'д' else \
(False if str_answer == 'n' or str_answer == 'н' else None)

if __name__ == '__main__':
    main()
