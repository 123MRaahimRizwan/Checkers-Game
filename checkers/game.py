import pygame
from .constants import BLACK, WHITE, GREYISH, SQUARE_SIZE
from checkers.board import Board


class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}
        self.win = win

    def update(self):
        """
        Updates the board
        """
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def reset(self):
        """
        Resets the position
        """
        self._init()

    def select(self, row, col):
        """
        Enables the user to select a piece
        """
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        """
        Enables a piece to move
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def winner(self):
        """
        Returns the winner
        """
        return self.board.winner()

    def draw_valid_moves(self, moves):
        """
        Draws valid moves on the board for the user
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREYISH, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def change_turn(self):
        """
        Changes turns "Self Explanatory"
        """
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def get_board(self):
        """
        Just returns the board object
        """
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
