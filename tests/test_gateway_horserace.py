"""gateway_horserace.pyのテスト."""
import datetime

import gateway_horserace
from data_transfer_objects import HorseEntry
from horseracelib.utility import HorseEntry as LibHorseEntry
from horseracelib.utility import HorseInfo


def test_get_horse_name(mocker):
    """get_horse_nameのテスト."""
    insmock = mocker.Mock()
    insmock.get_horse_info.return_value = HorseInfo(name='HORSENAME')
    mocker.patch.object(gateway_horserace, "Access",
                        mocker.Mock(return_value=insmock))
    horse_name = gateway_horserace.GatewayHorseRace().get_horse_name('01234567')
    assert horse_name == 'HORSENAME'
    assert insmock.get_horse_info.call_args_list == [(('01234567',),)]


def test_get_children_entries(mocker):
    """get_children_entriesのテスト."""
    insmock = mocker.Mock()
    insmock.iter_sire_entries.return_value = [
        LibHorseEntry(
            date=datetime.date(2018, 1, 1), course='川崎', raceno=1,
            racename='レース1', horsename='HORSE1'),
        LibHorseEntry(
            date=datetime.date(2018, 1, 2), course='名古屋', raceno=2,
            racename='レース2', horsename='HORSE2')
    ]
    mocker.patch.object(gateway_horserace, "Access",
                        mocker.Mock(return_value=insmock))
    entries = gateway_horserace.GatewayHorseRace().get_children_entries('01234567')
    assert entries == [
        HorseEntry(
            date=datetime.date(2018, 1, 1), course='川崎', raceno=1,
            racename='レース1', horsename='HORSE1'),
        HorseEntry(
            date=datetime.date(2018, 1, 2), course='名古屋', raceno=2,
            racename='レース2', horsename='HORSE2')
    ]
    assert insmock.iter_sire_entries.call_args_list == [(('01234567',),)]
