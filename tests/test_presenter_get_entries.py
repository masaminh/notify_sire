"""presenter_get_entries.pyのテスト."""
import datetime

from data_transfer_objects import HorseEntry, OutputDataGetEntries
from presenter_get_entries import PresenterGetEntries
from viewmodel_get_entries import ViewModelGetEntries


def test_complete(mocker):
    """completeのテスト."""
    view = mocker.Mock()
    output_data = OutputDataGetEntries(
        name='HORSE1',
        entries=[
            HorseEntry(
                date=datetime.date(2019, 1, 1), course='川崎', raceno=1,
                racename='RACE1', horsename='HORSE1')])
    PresenterGetEntries(view).complete(output_data)
    expected = [
        ((ViewModelGetEntries(name='HORSE1', entries=output_data.entries),),)]

    assert view.update.call_args_list == expected
