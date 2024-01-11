def get_first[T](lst: list[T]) -> T:
    return lst[0]


def get_first_str[T: str](lst: list[T]) -> T:
    """`T` could be `str` or any class inherited from `str` (i.e. we set type bound)"""
    return lst[0]


def flip[T, V](values: tuple[T, V]) -> tuple[V, T]:
    return (values[1], values[0])


print(get_first([1, 2, 3]))
print(get_first(["1", "2", "3"]))
