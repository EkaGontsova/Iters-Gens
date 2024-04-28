class FlatIterator:


    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_outer = 0
        self.current_inner = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.current_outer >= len(self.list_of_list):
            raise StopIteration

        while self.current_inner >= len(self.list_of_list[self.current_outer]):
            self.current_outer += 1
            self.current_inner = 0
            if self.current_outer >= len(self.list_of_list):
                raise StopIteration

        item = self.list_of_list[self.current_outer][self.current_inner]
        self.current_inner += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    print(list(FlatIterator(list_of_lists_1)))
