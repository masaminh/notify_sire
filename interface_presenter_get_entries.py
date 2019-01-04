"""出走予定取得時のプレセンターのインターフェイス."""

from abc import ABCMeta, abstractmethod
from data_transfer_objects import OutputDataGetEntries


class IPresenterGetEntries(metaclass=ABCMeta):
    """出走予定取得時のプレゼンター."""

    @abstractmethod
    def complete(self, output_data: OutputDataGetEntries) -> None:
        """出走予定取得時の出力."""
