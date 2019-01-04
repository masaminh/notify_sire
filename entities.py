"""エンティティ."""
import datetime

from dataclasses import dataclass


@dataclass
class HorseEntry:
    """出走予定."""

    date: datetime.date
    course: str
    raceno: int
    racename: str
    horsename: str
