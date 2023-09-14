import chess
from tkinter import *

WIDTH = 400
HEIGHT = 400
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE

window = Tk()
window.title("Chess")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

def draw_board():
    colours = ["white", "gray"]
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x1 = col * SQUARE_SIZE
            y1 = row * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            colour = colours[(row + col) % 2]
            canvas.create_rectangle(x1, y1, x2, y2, fill=colour)

def start_game():
    #draw_board()
    photo = PhotoImage(file="chesspieces\\b.png")
    label = Label(window, image=photo)
    #label.pack()
    # Change the location of the label on the canvas
    canvas.create_window(300, 300, anchor=NW, window=label)
    window.mainloop()


if __name__ == "__main__":
    start_game()
