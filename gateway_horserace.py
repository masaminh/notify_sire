"""horseracelibへのゲートウェイ."""
from typing import List

from entities import HorseEntry
from horseracelib.jbis import Access
from interface_gateway_horserace import IGatewayHorseRace


class GatewayHorseRace(IGatewayHorseRace):
    """horseracelibへのゲートウェイ."""

    def get_horse_name(self, horseid: str) -> str:
        """馬名の取得."""
        horseinfo = Access().get_horse_info(horseid)
        return horseinfo.name

    def get_children_entries(self, horseid: str) -> List[HorseEntry]:
        """出走予定の取得."""
        entries = Access().iter_sire_entries(horseid)
        entries_list = [
            HorseEntry(
                date=x.date, course=x.course, raceno=x.raceno,
                racename=x.racename, horsename=x.horsename) for x in entries]
        return entries_list
