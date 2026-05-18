from __future__ import annotations

from typing import Final
from collections.abc import Iterable, Iterator

class StrIterator(Iterator[tuple[int, str]]):
    __s: Final[str]
    __index: int

    def __init__(self, s: str) -> None:
        self.__s = s
        self.__index = 0

    def __next__(self) -> tuple[int, str]:
        if self.__index >= len(self.__s):
            raise StopIteration()
        result = (self.__index, self.__s[self.__index])
        self.__index += 1
        return result

class IndexIterator[T](Iterator[tuple[int, T]]):
    __underlying: Iterator[T]
    __index: int

    def __init__(self, coll: Iterable[T]) -> None:
        self.__underlying = iter(coll)
        self.__index = 0

    def __next__(self) -> tuple[int, T]:
        result = (self.__index, next(self.__underlying))
        self.__index += 1
        return result

def index_iterator[T](coll: Iterable[T]) -> Iterator[tuple[int, T]]:
    index = 0
    for x in coll:
        yield (index, x)
        index += 1

def map_positions_yield(width: int, height: int) -> Iterator[tuple[int, int]]:
    for x in range(width):
        for y in range(height):
            yield (x, y)

def map_positions_gen_expr(width: int, height: int) -> Iterator[tuple[int, int]]:
    return (
        (x, y)
        for x in range(width)
        for y in range(height)
    )

class MapPositionsIter(Iterator[tuple[int, int]]):
    __width: Final[int]
    __height: Final[int]
    __x: int
    __y: int

    def __init__(self, width: int, height: int) -> None:
        assert width > 0 and height > 0
        self.__width = width
        self.__height = height
        self.__x = 0
        self.__y = 0

    def __next__(self) -> tuple[int, int]:
        if self.__y >= self.__height:
            raise StopIteration()
        result = (self.__x, self.__y)
        if self.__x < self.__width - 1:
            self.__x += 1
        else:
            self.__x = 0
            self.__y += 1
        return result


def map_positions_class(width: int, height: int) -> Iterator[tuple[int, int]]:
    return MapPositionsIter(width, height)
