from typing import NamedTuple

class Foo(NamedTuple):
    bar: str
    baz: int
    qux: list

fred = Foo('hello',[], [1, 2])
print(fred)
