from typing import override


class Parent:
    def do_smthng(self, value: str) -> None:
        print(value)


class Child(Parent):
    @override
    def do_smthng(self, value: str) -> None:
        print("Value:", value)

    @override  # Warning from PyCharm here!
    def do_something(self, value: str) -> None:
        print("Value:", value)
