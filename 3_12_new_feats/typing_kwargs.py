from typing import TypedDict, Unpack


class Record(TypedDict):
    artist: str
    title: str
    year: int


def baz(**kwargs: Unpack[Record]):
    """See `Unpack` docstring for more info."""
    print(kwargs)


baz(artist="Burial", title="Untrue", year=2010)
