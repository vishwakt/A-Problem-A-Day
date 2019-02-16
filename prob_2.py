# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?


class Game(object):
    def __init__(self, array_of_numbers):
        self._array_of_numbers = array_of_numbers
        self._dictionary_of_products = {}
        self._product = 1
        self._print_list = list()

    def _get_product(self):
        for number in range(len(self._array_of_numbers)):
            self._product = self._product * self._array_of_numbers[number]

    def _get_list(self):
        for key in self._array_of_numbers:
            self._print_list.append(self._product / key)
        print self._print_list

    def get_output(self):
        self._get_product()
        self._get_list()


def main():
    prod = Game([1, 2, 3, 4, 5])
    prod.get_output()


if __name__ == "__main__":
    main()