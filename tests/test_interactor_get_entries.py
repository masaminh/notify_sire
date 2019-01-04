"""interactor_get_entries.pyのテスト."""
import datetime
from interactor_get_entries import InteractorGetEntries
from data_transfer_objects import InputDataGetEntries, OutputDataGetEntries, HorseEntry


def test_handle(mocker):
    """handleのテスト."""
    gateway = mocker.Mock()
    gateway.get_horse_name.return_value = 'HORSE'
    entries = [
        HorseEntry(
            date=datetime.date(2019, 1, 1), course='川崎', raceno=1,
            racename='RACE1', horsename='HORSE1'),
        HorseEntry(
            date=datetime.date(2019, 1, 2), course='浦和', raceno=2,
            racename='RACE2', horsename='HORSE2'),
    ]
    gateway.get_children_entries.return_value = entries
    presenter = mocker.Mock()

    interactor = InteractorGetEntries(gateway, presenter)
    interactor.handle(InputDataGetEntries(horseid='01234567'))

    assert gateway.get_horse_name.call_args_list == [(('01234567',),)]
    assert gateway.get_children_entries.call_args_list == [(('01234567',),)]
    expected = OutputDataGetEntries(name='HORSE', entries=entries)
    assert presenter.complete.call_args_list == [((expected,),)]
