"""Data Transfer Objects."""
from typing import List

from dataclasses import dataclass
from entities import HorseEntry


@dataclass
class InputDataGetEntries:
    """IUseCaseGetEntriesへの入力."""

    horseid: str


@dataclass
class OutputDataGetEntries:
    """IUserCaseGetEntriesの出力."""

    name: str
    entries: List[HorseEntry]
