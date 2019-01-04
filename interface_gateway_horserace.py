"""horseracelibへのゲートウェイ."""
from abc import ABCMeta, abstractmethod
from typing import List

from entities import HorseEntry


class IGatewayHorseRace(metaclass=ABCMeta):
    """horseracelibへのゲートウェイ."""

    @abstractmethod
    def get_horse_name(self, horseid: str) -> str:
        """馬名の取得."""

    @abstractmethod
    def get_children_entries(self, horseid: str) -> List[HorseEntry]:
        """出走予定の取得."""
