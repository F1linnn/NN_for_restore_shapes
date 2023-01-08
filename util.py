dict = {-1: '-', 1: '#'}


def to_text(x):
    return dict[x]


def f_activ(obraz):
    i = 0
    for g in obraz[0]:
        if g > 0:
            obraz[0][i] = 1
            i += 1
        elif g <= 0:
            obraz[0][i] = -1
            i += 1
    return obraz


def check(shapes, X):
    if 0 in X:
        return False
    obraz = ''
    obraz2 = ''
    check = []
    for i in shapes:
        for o in i:
            obraz += f"{to_text(o)}"
        check.append(obraz)
        obraz = ''
    for i in X:
        obraz2 += f"{to_text(i)}"
    # print()
    return obraz2 in check


def show_shape(obraz, size):
    i = 0
    for o in obraz:
        print(f"{to_text(o)}", end=''),
        i += 1
        if i % size == 0:
            print('\n')
