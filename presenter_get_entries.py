"""出走予定取得時のプレゼンター."""
from injector import inject

from data_transfer_objects import OutputDataGetEntries
from interface_presenter_get_entries import IPresenterGetEntries
from interface_view_get_entries import IViewGetEntries
from viewmodel_get_entries import ViewModelGetEntries


class PresenterGetEntries(IPresenterGetEntries):
    """出走予定取得時のプレゼンター."""

    @inject
    def __init__(self, view: IViewGetEntries):
        """コンストラクタ."""
        self.view = view

    def complete(self, output_data: OutputDataGetEntries) -> None:
        """出走予定取得時の出力."""
        viewmodel = ViewModelGetEntries(
            name=output_data.name, entries=output_data.entries)

        self.view.update(viewmodel)
