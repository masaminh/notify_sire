"""Line.pyのテスト."""
import line


def test_notify(mocker):
    """notifyのテスト."""
    mock = mocker.Mock()
    mocker.patch.object(line, 'requests', mock)
    line.notify('TOKEN', 'MESSAGE')
    expected = [
        (('https://notify-api.line.me/api/notify',),
         {'data': {'message': 'MESSAGE'}, 'headers': {'Authorization': 'Bearer TOKEN'}})
    ]

    assert mock.post.call_args_list == expected
