import pygame
import chess

# Pygame settings
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
CELL_SIZE = SCREEN_WIDTH // 8
WHITE = (169, 169, 169)  # Gray for white cells
BROWN = (139, 69, 19)  # Brown for black cells

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess Game")

# Create the chess board
board = chess.Board()

def draw_board():
    """Draws the chessboard and pieces as text."""
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
            # Draw the piece as text
            square = chess.square(col, 7 - row)
            piece = board.piece_at(square)
            if piece:
                font = pygame.font.SysFont(None, 48)
                piece_symbol = piece.symbol().upper() if piece.color == chess.WHITE else piece.symbol().lower()
                text = font.render(piece_symbol, True, (0, 0, 0) if piece.color == chess.WHITE else (255, 255, 255))
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 4))

def get_square_under_mouse():
    """Returns the square under the mouse cursor."""
    x, y = pygame.mouse.get_pos()
    col = x // CELL_SIZE
    row = 7 - (y // CELL_SIZE)
    return chess.square(col, row)

def handle_move(from_square, to_square):
    """Handles a move made by the player."""
    move = chess.Move(from_square, to_square)
    if move in board.legal_moves:
        board.push(move)
        return True
    return False

# Main game loop
running = True
selected_square = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            square = get_square_under_mouse()
            if selected_square:
                handle_move(selected_square, square)
                selected_square = None
            elif board.piece_at(square) and board.piece_at(square).color == board.turn:
                selected_square = square

    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()

pygame.quit()
