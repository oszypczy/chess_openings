import csv
import re


def get_openings(path):
    with open(path, 'r') as handle:
        return read_opening(handle)


def get_game(path):
    with open(path, 'r') as handle:
        return format_moves(handle.read())


def read_opening(handle):
    data = []
    reader = csv.DictReader(handle)
    for row in reader:
        name = row['name']
        moves = row['moves']
        opening = Opening(name, format_moves(moves))
        data.append(opening)
    return data


def format_moves(moves):
    list_of_moves = re.split(r'\d+\.', moves)
    content = [move.rstrip() for move in list_of_moves if move]
    return content


class Opening:
    def __init__(self, name, moves) -> None:
        self.name = name
        self.moves = moves
