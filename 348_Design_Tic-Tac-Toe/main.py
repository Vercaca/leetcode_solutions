
# Initialize your data structure here.
class TicTacToe:
    def __init__(self, n):
        self.board = [[0] *n  for _ in range(n)]
        self.n = n
        self.rows = [[0,0] for _ in range(n)]
        self.cols = [[0,0] for _ in range(n)]

    def move(self, i, j, player):

        self.board[i][j] = player
        result = self.is_win(i, j, player)
        print('\n>> player {} moves at: ({}, {})'.format(player, i, j))
        print(self)
        print(result)
        return result

    def is_win(self, i, j, player):
        print(self.rows)
        print(self.cols)
        # check row
        if self.rows[i][player-1] == self.n-1:
            if self.board[i] == [player] * self.n:
                return 1

        # check col
        if self.cols[j][player-1] == self.n-1:
            col = [self.board[row][j] for row in range(self.n)]
            if col == [player] * self.n:
                return 1

        # check diagonal
        if i == j:
            line = [self.board[num][num] for num in range(self.n)]
            if line == [player] * self.n:
                return 1
        if i+j == self.n-1:
            line = [self.board[num][self.n-num-1] for num in range(self.n)]
            if line == [player] * self.n:
                return 1

        # add to potential lose_rows
        self.rows[i][player-1] += 1
        self.cols[j][player-1] += 1


        return 0

    def __repr__(self):
        # print(self.board)
        s = ''
        for i in range(len(self.board)):
            s+= '|'.join([str(j) for j in self.board[i]]).replace('0', ' ')\
                        .replace('1', 'O').replace('2', 'X')
            s+= '\n'
        return s


if __name__ == '__main__':

    game = TicTacToe(3)

    game.move(0, 1, 1)
    game.move(1, 2, 2)
    game.move(0, 2, 1)
    game.move(0, 0, 2)
    game.move(1, 1, 1)
    game.move(2, 0, 2)
    game.move(2, 1, 1)
