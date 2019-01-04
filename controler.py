"""コントローラー."""
from injector import inject
from interface_usecase_get_entries import IUseCaseGetEntries
from data_transfer_objects import InputDataGetEntries


class Controler:
    """コントローラー."""

    @inject
    def __init__(self, usecase_get_entries: IUseCaseGetEntries):
        """コンストラクタ."""
        self.usecase_get_entries = usecase_get_entries

    def get_entries(self, horseid: str) -> None:
        """出走予定の取得."""
        input_data = InputDataGetEntries(horseid=horseid)
        self.usecase_get_entries.handle(input_data)
