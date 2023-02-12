import sys
import argparse
from zaliczenie_szachy_io import get_openings, get_game


class NoMatchingOpeningsError(Exception):
    pass


class EmptyGameError(Exception):
    pass


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("openings_file")
    parser.add_argument("game_file")
    args = parser.parse_args(arguments[1:])
    openings = get_openings(args.openings_file)
    game = get_game(args.game_file)
    outcome = []
    for each_opening in openings:
        for index, each_move in enumerate(each_opening.moves):
            try:
                if each_move != game[index]:
                    break
            except IndexError:
                raise EmptyGameError("The game has no moves!")
        else:
            outcome.append((len(each_opening.moves), each_opening.name))
    if not outcome:
        raise NoMatchingOpeningsError("No openings match with this game.")
    outcomes_sorted = sorted(outcome, reverse=True)
    print(f"Openig used in this game is called: {outcomes_sorted[0][1]}")


if __name__ == "__main__":
    main(sys.argv)
