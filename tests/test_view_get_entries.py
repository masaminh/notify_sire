"""view_get_entries.pyのテスト."""
import datetime

import view_get_entries
from data_transfer_objects import HorseEntry
from viewmodel_get_entries import ViewModelGetEntries


def test_console_update(mocker):
    """ViewGetEntriesConsole.updateのテスト."""
    print_mock = mocker.Mock()
    mocker.patch.object(view_get_entries, "print", print_mock)
    viewmodel = ViewModelGetEntries(
        name='HORSE1', entries=[
            HorseEntry(
                date=datetime.date(2019, 1, 1), course='川崎', raceno=1,
                racename='RACE1', horsename='HORSE2')])
    view_get_entries.ViewGetEntriesConsole().update(viewmodel)
    expected_content = 'HORSE1産駒の出走予定\n\n01/01\n　川崎1R RACE1\n　　HORSE2\n'
    assert print_mock.call_args_list == [((expected_content,),)]


def test_line_update(mocker):
    """ViewGetEntriesLine.updateのテスト."""
    settings_mock = mocker.Mock()
    mocker.patch.object(view_get_entries, 'settings', settings_mock)
    settings_mock.NOTIFY_ACCESS_TOKEN = 'TOKEN'
    line_mock = mocker.Mock()
    mocker.patch.object(view_get_entries, "line", line_mock)
    viewmodel = ViewModelGetEntries(
        name='HORSE1', entries=[
            HorseEntry(
                date=datetime.date(2019, 1, 1), course='川崎', raceno=1,
                racename='RACE1', horsename='HORSE2')])
    view_get_entries.ViewGetEntriesLine().update(viewmodel)
    expected_content = 'HORSE1産駒の出走予定\n\n01/01\n　川崎1R RACE1\n　　HORSE2\n'
    assert line_mock.notify.call_args_list == [(('TOKEN', expected_content,),)]


def test_get_content_nothing():
    """get_contentのテスト(出走予定がないとき)."""
    viewmodel = ViewModelGetEntries(name='HORSE1', entries=[])
    expected = 'HORSE1産駒の出走予定\n　なし\n'
    assert view_get_entries.get_content(viewmodel) == expected
