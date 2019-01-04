"""controler.pyのテスト."""

from controler import Controler
from data_transfer_objects import InputDataGetEntries


def test_controler_get_entries(mocker):
    """get_entriesのテスト."""
    mock = mocker.Mock()
    controler = Controler(mock)
    controler.get_entries('01234567')
    expected = [((InputDataGetEntries(horseid='01234567'),),)]
    assert mock.handle.call_args_list == expected
