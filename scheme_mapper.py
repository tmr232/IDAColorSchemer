import itertools
import re

COLOR_PAT = re.compile(r'^([0-9a-f]{6})\t')


def repl_maker():
    counter = itertools.count()

    def repl(m):
        return f'{next(counter):06x}\t'

    return repl


def main():
    with open('ugly.clr', 'r') as f:
        lines = f.readlines()

    repl = repl_maker()
    for line in lines:
        print(COLOR_PAT.sub(repl, line))


if __name__ == '__main__':
    main()
