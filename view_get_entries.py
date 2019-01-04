"""出走予定のビュー."""
from itertools import groupby

import line
import mojimoji
from interface_view_get_entries import IViewGetEntries
from viewmodel_get_entries import ViewModelGetEntries
import settings


class ViewGetEntriesConsole(IViewGetEntries):
    """出走予定のビュー."""

    def update(self, viewmodel: ViewModelGetEntries)->None:
        """出力."""
        content = get_content(viewmodel)
        print(content)


class ViewGetEntriesLine(IViewGetEntries):
    """出走予定のビュー."""

    def update(self, viewmodel: ViewModelGetEntries)->None:
        """出力."""
        content = get_content(viewmodel)
        line.notify(settings.NOTIFY_ACCESS_TOKEN, content)


def get_racename_line(course: str, raceno: int, racename: str) -> str:
    """レース名行の取得."""
    racename = mojimoji.zen_to_han(racename, kana=False)
    return f'{course}{raceno}R {racename}'


def get_content(viewmodel: ViewModelGetEntries) -> str:
    """出力文字列の取得."""
    content = f'{viewmodel.name}産駒の出走予定\n'

    if viewmodel.entries:
        for date, group in groupby(viewmodel.entries, lambda x: x.date):
            content += f'\n{date.strftime("%m/%d")}\n'
            for race, group2 in groupby(group, lambda x: (x.course, x.raceno, x.racename)):
                content += '　' + get_racename_line(*race) + '\n'
                for scheduled in group2:
                    content += f'　　{scheduled.horsename}\n'
    else:
        content += '　なし\n'

    return content
