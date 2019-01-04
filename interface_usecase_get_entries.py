"""出走予定取得ユースケースのインターフェイス."""
from abc import ABCMeta, abstractmethod

from data_transfer_objects import InputDataGetEntries


class IUseCaseGetEntries(metaclass=ABCMeta):
    """出走予定取得ユースケースのインターフェイス."""

    @abstractmethod
    def handle(self, input_data: InputDataGetEntries) -> None:
        """出走予定取得."""
