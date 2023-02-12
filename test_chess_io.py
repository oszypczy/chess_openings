from io import StringIO
from zaliczenie_szachy_io import read_opening, get_game
import argparse
import os


def test_read_openings():
    data = '"ECO","name","moves"\r\n"A00","Anderssens Opening","1.a3"\r\n"A00","Polish Gambit","1.a3 a5 2.b4"\r\n' # noqa 551
    handle = StringIO(data)
    openings = read_opening(handle)
    assert openings[0].name == "Anderssens Opening"
    assert openings[0].moves == ['a3']
    assert openings[1].name == "Polish Gambit"
    assert openings[1].moves == ['a3 a5', 'b4']


def test_get_game():
    data = "1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 7.Qe2 b5 8.Qe5 9.Bxc7" # noqa 551
    with open('game.txt', 'w') as handle:
        handle.write(data)
    args = argparse.Namespace(game_file="game.txt")
    game = get_game(args.game_file)
    assert game == ['d4 d5', 'c4 dxc4', 'Nf3 Nf6', 'e3 e6', 'Bxc4 c5', 'O-O a6', 'Qe2 b5', 'Qe5', 'Bxc7'] # noqa 551
    os.remove('game.txt')
