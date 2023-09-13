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


@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(debug=True)
    board = chess.Board()
    print(board.is_checkmate())
    # FOOL's MATE
    board.push_san("e4")
    print(board)
    board.push_san("g5")
    print(board)
    board.push_san("Nc3")
    print(board)
    board.push_san("f5")
    print(board)
    board.push_san("Qh5")
    print(board)
    print(board.is_checkmate())