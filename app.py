from flask import Flask, render_template, request, redirect, url_for
import chess

#region Helpful commands
""" 
board.legal_moves : list of legal moves for white/black depending on whose turn it is.
board.is_checkmate() : boolean, tells if game over
board.push_san() : move to make
"""
#endregion


app = Flask(__name__)

def boardToString(board):
    new_board = ""
    for i in str(board):
        if i == "\n":
            new_board += "_"
        else:
            new_board += i
    return new_board


@app.route('/')
def home():
    board = chess.Board()
    return render_template("index.html", board=boardToString(board))

if __name__ == '__main__':
    app.run(debug=True)
    """
    board = chess.Board()
    while True:
        if board.is_checkmate():
            print("GAME OVER!0")
            break
        print(board)
        try:
            board.push_san(input("Enter the move: "))
        except Exception:
            print("DO A VALID MOVE!")
    """