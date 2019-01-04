"""指定種牡馬産駒の出走予定を通知する."""
from argparse import ArgumentParser

from injector import Injector, Module

from controler import Controler
from gateway_horserace import GatewayHorseRace
from interactor_get_entries import InteractorGetEntries
from interface_gateway_horserace import IGatewayHorseRace
from interface_presenter_get_entries import IPresenterGetEntries
from interface_usecase_get_entries import IUseCaseGetEntries
from interface_view_get_entries import IViewGetEntries
from presenter_get_entries import PresenterGetEntries
from view_get_entries import ViewGetEntriesConsole, ViewGetEntriesLine


def main():
    """メイン関数."""
    parser = ArgumentParser(description='指定種牡馬産駒の出走予定をLINE Notifyに送る')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='デバッグ用(コンソール出力)')
    parser.add_argument('horseid', nargs='+', help='馬番号')
    args = parser.parse_args()
    horseids = args.horseid

    module = LineDiModule() if not args.debug else ConsoleDiModule()
    injector = Injector([module])
    controler = injector.get(Controler)

    for horseid in horseids:
        controler.get_entries(horseid)


class ConsoleDiModule(Module):
    """コンソール出力用."""

    def configure(self, binder):
        """インターフェイスと実装の紐づけ."""
        binder.bind(IUseCaseGetEntries, InteractorGetEntries)
        binder.bind(IGatewayHorseRace, GatewayHorseRace)
        binder.bind(IPresenterGetEntries, PresenterGetEntries)
        binder.bind(IViewGetEntries, ViewGetEntriesConsole)


class LineDiModule(Module):
    """コンソール出力用."""

    def configure(self, binder):
        """インターフェイスと実装の紐づけ."""
        binder.bind(IUseCaseGetEntries, InteractorGetEntries)
        binder.bind(IGatewayHorseRace, GatewayHorseRace)
        binder.bind(IPresenterGetEntries, PresenterGetEntries)
        binder.bind(IViewGetEntries, ViewGetEntriesLine)


if __name__ == "__main__":
    main()
