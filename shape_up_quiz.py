symbols = ['C', 'D', 'S', 'T']


class Rule:
    def __init__(self, index, pos, symbol):

        self.index = index
        self.pos = pos
        self.symbol = symbol

    def get_strip(self, cells):
        pass

    def set_strip(self, cells, strip):
        return cells

    def get_index(self, row, col):
        return '{r}{c}'.format(r=row, c=col)

    def eliminate(self, cells):
        """Remove all of self.symbol from cells where they can't exist"""
        strip = self.get_strip(cells)
        if self.pos == 0:
            # cant exist in 3,4,5
            del_map = '   XXX'
        elif self.pos == 3:
            del_map = 'XXX   '
        elif self.pos == 1:
            del_map = 'X   XX'
        else:
            del_map = 'XX   X'

        for idx in range(0, 6):
            if del_map[idx] == 'X':
                strip[idx] = strip[idx].replace(self.symbol, '')

        return self.set_strip(cells, strip)

    def eliminate2(self, cells):
        # now remove all other symbols (except B) from where they can't exist
        strip = self.get_strip(cells)
        if self.pos == 0:
            for c in symbols:
                if c != self.symbol:
                    strip[0] = strip[0].replace(c, '')
        elif self.pos == 3:
            for c in symbols:
                if c != self.symbol:
                    strip[5] = strip[5].replace(c, '')

        return self.set_strip(cells, strip)

    def __repr__(self):
        return 'Rule: {i} {p} {s}'.format(p=self.pos, s=self.symbol, i=self.index)


class RowRule(Rule):
    def __init__(self, index, pos, symbol):
        super(RowRule, self).__init__(index, pos, symbol)

    def get_strip(self, cells):
        strip = []
        for col in range(0, 6):
            idx = self.get_index(self.index, col)
            strip.append(cells[idx])
        return strip

    def set_strip(self, cells, strip):
        for col in range(0, 6):
            idx = self.get_index(self.index, col)
            cells[idx] = strip[col]
        return cells

    def __repr__(self):
        return 'Rule: Row: {i} {p} {s}'.format(p=self.pos, s=self.symbol, i=self.index)


class ColRule(Rule):
    def __init__(self, index, pos, symbol):
        super(ColRule, self).__init__(index, pos, symbol)

    def get_strip(self, cells):
        strip = []
        for row in range(0, 6):
            idx = self.get_index(row, self.index)
            strip.append(cells[idx])
        return strip

    def set_strip(self, cells, strip):
        for row in range(0, 6):
            idx = self.get_index(row, self.index)
            cells[idx] = strip[row]
        return cells

    def __repr__(self):
        return 'Rule: Col:{i} {p} {s}'.format(p=self.pos, s=self.symbol, i=self.index)


def print_cells(cells):
    for r in range(0, 6):
        row = ''
        for c in range(0, 6):
            idx = str(r) + str(c)
            row = row + '{c:6s} '.format(c=cells[idx])
        print(row)


def keep_only(cells, symbol, keep_row, keep_col):
    for r in range(0, 6):
        if r != keep_row:
            idx = str(r) + str(keep_col)
            cells[idx] = cells[idx].replace(symbol, '')
    for c in range(0, 6):
        if c != keep_col:
            idx = str(keep_row) + str(c)
            cells[idx] = cells[idx].replace(symbol, '')
    idx = '{r}{c}'.format(r=keep_row, c=keep_col)
    cells[idx] = symbol
    return cells


if __name__ == "__main__":

    rules = [
        ColRule(0, 1, 'C'),
        ColRule(0, 3, 'S'),
        ColRule(2, 0, 'C'),
        ColRule(3, 3, 'C'),
        ColRule(4, 0, 'D'),
        ColRule(4, 2, 'S'),

        RowRule(0, 1, 'C'),
        RowRule(0, 3, 'T'),
        RowRule(1, 0, 'T'),
        RowRule(1, 3, 'C'),
        RowRule(2, 0, 'S'),
        RowRule(2, 3, 'C'),
        RowRule(3, 1, 'T'),
        RowRule(4, 1, 'D'),
        RowRule(5, 2, 'D')
    ]

    cells = {}
    for r in range(0, 6):
        for c in range(0, 6):
            idx = str(r) + str(c)
            # print(idx)
            cells[idx] = 'CDSTB'
    print(cells)
    # print(rules)

    cells = keep_only(cells, 'C', 5, 3)
    cells = keep_only(cells, 'T', 5, 1)
    cells = keep_only(cells, 'S', 5, 0)

    cells = keep_only(cells, 'S', 4, 4)
    cells = keep_only(cells, 'T', 4, 0)

    for rule in rules:
        try:
            print('Eliminate1: {}'.format(rule))
            cells = rule.eliminate(cells)
            print_cells(cells)
        except TypeError:
            print('Failed on rule:' + str(rule))
            exit(1)

    for rule in rules:
        try:
            print('Eliminate2: {}'.format(rule))
            cells = rule.eliminate2(cells)
            print_cells(cells)
        except TypeError:
            print('Failed on rule:' + str(rule))
            exit(1)

    for reduce in range(0, 4):
        print('Reduction: {r}'.format(r=reduce))
        for r in range(0, 6):
            for s in symbols:
                exists_in = []
                for c in range(0, 6):
                    idx = str(r) + str(c)
                    if s in cells[idx]:
                        exists_in.append(c)
                if len(exists_in) == 1:
                    print('{s} only in row {r} col {c}'.format(s=s, r=r, c=exists_in[0]))
                    cells = keep_only(cells, s, r, exists_in[0])
                    print_cells(cells)
        for c in range(0, 6):
            for s in symbols:
                exists_in = []
                for r in range(0, 6):
                    idx = str(r) + str(c)
                    if s in cells[idx]:
                        exists_in.append(r)
                if len(exists_in) == 1:
                    print('{s} only in row {r} col {c}'.format(s=s, r=r, c=exists_in[0]))
                    cells = keep_only(cells, s, exists_in[0], c)
                    print_cells(cells)
