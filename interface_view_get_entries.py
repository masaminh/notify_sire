"""出走予定のビュー."""
from abc import ABCMeta, abstractmethod

from viewmodel_get_entries import ViewModelGetEntries


class IViewGetEntries(metaclass=ABCMeta):
    """出走予定のビューのインターフェイス."""

    @abstractmethod
    def update(self, viewmodel: ViewModelGetEntries)->None:
        """出力."""
