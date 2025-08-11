class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.diags = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[(player, row)] += 1
        self.cols[(player, col)] += 1

        if not row - col:
            self.diags[(player, row - col)] += 1
        
        if row + col == self.n - 1:
            self.diags[(player, row + col)] += 1

        if self.rows[(player, row)] == self.n or self.cols[(player, col)] == self.n or self.diags[(player, row - col)] == self.n or self.diags[(player, row + col)] == self.n:
            return player 
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
