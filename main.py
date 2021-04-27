from tkinter import *


root = Tk()
root.title('Black Jack')
root.maxsize(900, 800)
root.config(bg='darkorange')


def start():
    pass


def hit():
    pass
    # wordBased.hit()


def hold():
    pass
    #wordBased.hold()


# Frame/Base layout ---------------------------------------------------------------------------------------------------


UI_frame = Frame(root, width=800, height=100, bg='lightgray')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=800, height=350, bg='bisque')
canvas.grid(row=1, column=0, padx=10, pady=5)

output = Canvas(root, width=800, height=125, bg='bisque')
output.grid(row=2, column=0, padx=10, pady=5)

# User Interface Area -------------------------------------------------------------------------------------------------

# ------Row[0]------
# Number of players
num_of_players = Scale(UI_frame, bg="bisque", from_=1, to=3, length=180, resolution=1, orient=HORIZONTAL,
                       label="Select number of players below:")
num_of_players.grid(row=0, column=0, padx=5, pady=5)

# Number of decks
num_of_decks = Scale(UI_frame,  bg="bisque", from_=1, to=10, length=180, resolution=1, orient=HORIZONTAL,
                     label="Select number of decks to use:")
num_of_decks.grid(row=0, column=2, padx=5, pady=5)

# Start button
Button(UI_frame, text="  START  ", command=start(), bg='mediumseagreen').grid(row=0, column=3, padx=5, pady=5)

# ------Row[1]------
# Hit button
Button(UI_frame, text="  HIT  ", command=hit(), bg='papayawhip').grid(row=1, column=3, padx=5, pady=5)


# Hold button
Button(UI_frame, text=" HOLD ", command=hold(), bg='papayawhip').grid(row=1, column=4, padx=5, pady=5, sticky=E)

root.mainloop()
