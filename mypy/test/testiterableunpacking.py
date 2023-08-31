import typing

class Spam:
    def __iter__(self, /) -> typing.Iterator[int]:
        yield 1

a = Spam()

# list[int]
reveal_type(list(a))

# list[int]
reveal_type([i for i in a])

# list[int]
reveal_type([*(i for i in a)])

# list[int]
reveal_type([*a.__iter__()])

# list[Any] ???
reveal_type([*a])

b, = a
# int
reveal_type(b)