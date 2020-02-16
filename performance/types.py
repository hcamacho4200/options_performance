from enum import Enum


class Instruction(Enum):
    OPENING = 1
    CLOSING = 2


class AssetType(Enum):
    EQUITY = 1
    OPTION = 2
    CASH_EQUIVALENT = 3


