from random import shuffle

BUTTONPOSITION = {
    '0': {'row': 4, 'column': 2},
    '1': {'row': 3, 'column': 1},
    '2': {'row': 3, 'column': 2},
    '3': {'row': 3, 'column': 3},
    '4': {'row': 2, 'column': 1},
    '5': {'row': 2, 'column': 2},
    '6': {'row': 2, 'column': 3},
    '7': {'row': 1, 'column': 1},
    '8': {'row': 1, 'column': 2},
    '9': {'row': 1, 'column': 3},
    '+': {'row': 1, 'column': 5},
    '-': {'row': 2, 'column': 5},
    'x': {'row': 3, 'column': 5},
    '/': {'row': 4, 'column': 5},
    '<<': {'row': 1, 'column': 4},
    '=': {'row': 4, 'column': 4}
}


def scramble_positions():
    keys, vals = [[k for k, v in BUTTONPOSITION.items()],
                  [v for k, v in BUTTONPOSITION.items()]]
    shuffle(keys)
    return dict(zip(keys, vals))


if __name__ == '__main__':
    print(scramble_positions())
