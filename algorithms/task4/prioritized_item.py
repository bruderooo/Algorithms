from dataclasses import astuple, dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)

    def __iter__(self):
        return iter(astuple(self))
