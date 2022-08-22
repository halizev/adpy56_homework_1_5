import main

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.iter_cursor = -1
        self.iter_list_len = len(self.iter_list)

    def __iter__(self):
        self.iter_cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.iter_list[self.iter_cursor]):
            iter(self)
        if self.iter_cursor == self.iter_list_len:
            raise StopIteration
        self.nest_cursor += 1
        return self.iter_list[self.iter_cursor][self.nest_cursor - 1]


@main.parametrized_decorator('log_file.txt')
def flat_generator(iter_list, ignore_types=(str)):
    for x in iter_list:
        if hasattr(x, '__iter__') and not isinstance(x, ignore_types):
            yield from flat_generator(x)
        else:
            yield x


iterator_list = [item for item in FlatIterator(nested_list)]
print(iterator_list)

for item in FlatIterator(nested_list):
    print(item)

generator_list = [item for item in flat_generator(nested_list)]
print(generator_list)

for item in flat_generator(nested_list):
    print(item)