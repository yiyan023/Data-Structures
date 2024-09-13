class TicTacToe:
    def __init__(self, n: int):
        self.row = {1: defaultdict(set), 2: defaultdict(set)}
        self.col = {1: defaultdict(set), 2: defaultdict(set)}
        self.diag = {1: {"x==y": set(), "n-x==y": set()}, 2: {"x==y": set(), "n-x==y": set()}}
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.row[player][(row)].add((row, col))
        self.col[player][(col)].add((row, col))
        self.diag[player]["x==y"].add((row, col)) if row == col else None
        self.diag[player]["n-x==y"].add((row, col)) if self.n - col == row + 1 else None

        row_full, col_full = len(self.row[player][(row)]) == self.n, len(self.col[player][(col)]) == self.n
        diag_full = len(self.diag[player]["x==y"]) == self.n or len(self.diag[player]["n-x==y"]) == self.n

        if row_full or col_full or diag_full:
            return player

        return 0
