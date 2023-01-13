import pygame

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.width = 400
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tic Tac Toe")
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = 1
        self.winner = 0
        self.font = pygame.font.Font(None, 32)

    def draw_board(self):
        self.screen.fill((255, 255, 255)) # fill the screen with white
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(self.screen, (200, 200, 200), (i*self.width//3, j*self.height//3, self.width//3, self.height//3), 0)
                if self.board[i][j] == 1:
                    self.draw_x(i, j)
                elif self.board[i][j] == 2:
                    self.draw_o(i, j)
        for i in range(1,3):
            pygame.draw.line(self.screen, (0, 0, 0), (i*self.width//3, 0), (i*self.width//3, self.height), 2)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i*self.height//3), (self.width, i*self.height//3), 2)


    def draw_x(self, i, j):
        pygame.draw.line(self.screen, (0, 0, 0), (i*self.width//3+10, j*self.height//3+10), ((i+1)*self.width//3-10, (j+1)*self.height//3-10), 3)
        pygame.draw.line(self.screen, (0, 0, 0), (i*self.width//3+10, (j+1)*self.height//3-10), ((i+1)*self.width//3-10, j*self.height//3+10), 3)

    def draw_o(self, i, j):
        pygame.draw.circle(self.screen, (0, 0, 0), (i*self.width//3+self.width//6, j*self.height//3+self.height//6), self.width//6-10, 3)

    def check_winner(self):
        # check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
                self.winner = self.board[i][0]
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
                self.winner = self.board[0][i]
                return True
        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            self.winner = self.board[0][0]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
            self.winner = self.board[0][2]
            return True
        return False

    def draw_result(self):
        caption = "Tic Tac Toe - Player {} wins!".format(self.winner)
        pygame.display.set_caption(caption)
        pygame.time.delay(3000)

    def run(self):
        running = True
        move_made = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.winner == 0:
                    x, y = pygame.mouse.get_pos()
                    i = x // (self.width // 3)
                    j = y // (self.height // 3)
                    if self.board[i][j] == 0:
                        self.board[i][j] = self.player
                        move_made = True
                        
            self.screen.fill((255, 255, 255))
            self.draw_board()
            pygame.display.update()
            
            if move_made:
                move_made = False
                if self.check_winner():
                    self.draw_result()
                    running = False
                else:
                    self.player = 3 - self.player

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
    pygame.quit()

