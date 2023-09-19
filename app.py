from flask import Flask, render_template, request, redirect, url_for, jsonify
import chess
from stockfish import Stockfish

#region Helpful commands
""" 
board.legal_moves : list of legal moves for white/black depending on whose turn it is.
board.is_checkmate() : boolean, tells if game over
board.push_san() : move to make
"""
#endregion

board = chess.Board()
app = Flask(__name__)

def boardToString(board):
    new_board = ""
    for i in str(board):
        if i == "\n" or i == " ":
            pass
        else:
            new_board += i
    return new_board

@app.route('/')
def index():
    global board
    board = chess.Board()
    #return redirect(url_for('home'))
    return redirect(url_for('stockfish'))

@app.route('/home', methods=['GET', 'POST'])
def home():
    global board
    if request.method == 'GET':
        return render_template("index.html", board=boardToString(board))
    if request.method == 'POST':
        square = ""
        capture = ""
        if request.form.get('move').lower() == "reset":
            board = chess.Board()
            return jsonify(board=boardToString(board))
        else:
            if "x" in request.form.get('move'):
                foundX = False
                for i in request.form.get('move'):
                    if i == "x":
                        foundX = True
                    elif foundX:
                        square += i
                capture = board.piece_at(chess.parse_square(square))
            board.push_san(request.form.get('move'))
            print(capture)
            return jsonify(board=boardToString(board), state="c", capture=str(capture))


@app.route('/stockfish', methods=['GET', 'POST'])
def stockfish():
    global board
    if request.method == 'GET':
        return render_template("index.html", board=boardToString(board))
    if request.method == 'POST':
        square = ""
        capture = ""
        if request.form.get('move').lower() == "reset":
            board = chess.Board()
            return jsonify(board=boardToString(board))
        else:
            if "x" in request.form.get('move'):
                foundX = False
                for i in request.form.get('move'):
                    if i == "x":
                        foundX = True
                    elif foundX:
                        square += i
                capture = board.piece_at(chess.parse_square(square))
            board.push_san(request.form.get('move'))
            print(capture)
            return jsonify(board=boardToString(board), state="c", capture=str(capture))


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