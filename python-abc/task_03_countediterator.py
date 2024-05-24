#!/usr/bin/env python3
"""create class CountedIterator that extends the built-in """

class CountedIterator:
    def __init__(self, it_elmt):
        self.iter = iter(it_elmt)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            element = next(self.iter)
            self.count += 1
            return element
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        return self
