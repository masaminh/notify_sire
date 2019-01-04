"""出走予定取得時のViewModel."""
from typing import List

from data_transfer_objects import HorseEntry
from dataclasses import dataclass


@dataclass
class ViewModelGetEntries:
    """出走予定取得時のViewModel."""

    name: str
    entries: List[HorseEntry]
