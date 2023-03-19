from enum import Enum
from typing import NamedTuple
from investments.money import Money

class CorporateActionKind(Enum):
    TenderOddLots = 1

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.value < other.value

class CorporateAction(NamedTuple):
    description: str
    kind: CorporateActionKind