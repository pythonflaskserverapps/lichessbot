import chess

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

def test_board():
    board = chess.Board()
    fen = board.fen()
    print("start fen",START_FEN)
    print("board fen",fen)
    print("testing equality...")
    assert board.fen() == START_FEN
    print("passed")

