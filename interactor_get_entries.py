"""出走予定取得用interactor."""
from injector import inject

from data_transfer_objects import InputDataGetEntries, OutputDataGetEntries
from interface_gateway_horserace import IGatewayHorseRace
from interface_presenter_get_entries import IPresenterGetEntries
from interface_usecase_get_entries import IUseCaseGetEntries


class InteractorGetEntries(IUseCaseGetEntries):
    """出走予定取得用interactor."""

    @inject
    def __init__(self, gateway: IGatewayHorseRace, presenter: IPresenterGetEntries):
        """コンストラクタ."""
        self.gateway = gateway
        self.presenter = presenter

    def handle(self, input_data: InputDataGetEntries) -> None:
        """出走予定取得."""
        horseid = input_data.horseid
        name = self.gateway.get_horse_name(horseid)
        entries = self.gateway.get_children_entries(horseid)
        output_data = OutputDataGetEntries(name=name, entries=entries)
        self.presenter.complete(output_data)
