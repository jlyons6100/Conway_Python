
import tkinter as tk
import Conway
import cProfile
import copy

# Basic Tkinter App for visualizing Conway's Game of Life
class Application(tk.Frame):
    #__init__: Creates app for conway board from input parameters
    def __init__(self, n_squares, chance_zero, master=None):
        super().__init__(master)
        self.n_squares = n_squares
        self.chance_zero = chance_zero
        self.g = Conway.Game(self.n_squares,self.chance_zero)
        self.g.create_board()
        #self.g.create_board()
        self.brd = self.g.return_board()
        self.prev_brd = copy.deepcopy(self.brd)
        self.prev_prev_brd = None
        self.drawn = []
        self.master = master
        self.pack()
        self.create_widgets()

    # step: Getting the next n generations and repainting the board afterwards
    def step(self, n):
        for i in range(n):
            self.g.next_gen() # .102 seconds, .92 seconds after taking out extra if states in Conway
        self.repaint_board() # .102 seconds for 80x80, repaint .048 with deepcopy of array to only modify changes

    # change_state: Whether or not the game is running.
    def change_state(self):
        global text_map
        if str(text_map["Start Button"].get()) == "Stop":
            text_map["Start Button"].set("Start")
        else:
            text_map["Start Button"].set("Stop")

    # repaint_board: Repaints the squares that make up the board. Live squares - Dark blue, Recently Dead squares - Light blue, Dead squares - Black
    def repaint_board(self):
        for row in range(self.n_squares):
            for col in range(self.n_squares):
                if self.prev_brd[row][col] != self.brd[row][col]:
                    if self.brd[row][col] == 1: self.canvas.itemconfig(self.drawn[row][col], fill="#3471ab")
                    elif self.prev_brd[row][col] == 1: self.canvas.itemconfig(self.drawn[row][col], fill="#71a4d4")
                    else: self.canvas.itemconfig(self.drawn[row][col], fill="black")
                else:
                    self.canvas.itemconfig(self.drawn[row][col], fill="black")
        self.prev_brd = copy.deepcopy(self.brd)

    # create_widgets: Start and stop buttons from state widget. Canvas for drawing board.
    def create_widgets(self):
        self.state = tk.Button(self, text="Start", width=10,textvariable=text_map["Start Button"],command=self.change_state)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        c_diam = 750
        s_w = c_diam/self.n_squares #Square width
        self.canvas = tk.Canvas(self, width = c_diam, height = c_diam, background="black")
        canvas = self.canvas
        for row in range(self.n_squares):
            self.drawn.append([])
            for col in range(self.n_squares):
                if self.brd[row][col] == 1: c = self.canvas.create_rectangle(row*s_w, col*s_w, (row+1)*s_w, (col+1)*s_w, outline="#000", fill="#3471ab") # x1 y1 x2 y2
                else: c = self.canvas.create_rectangle(row*s_w, col*s_w, (row+1)*s_w, (col+1)*s_w, outline="#000", fill="black") 
                self.drawn[row].append(c)
        self.canvas.pack(side="top")
        self.quit.pack(side="bottom")
        self.state.pack(side="bottom")

root = tk.Tk()

# text_map: Stores text_variables, strings that display dynamic text in Tkinter
text_map = {}
def get_text_variables():
    global text_map
    text_var = tk.StringVar(root)
    text_var.set("Start")
    text_map["Start Button"] = (text_var)
get_text_variables()
screen_size = "1000"
root.geometry(screen_size + "x" + screen_size) #
app = Application(50, .75, master=root) # 50x50 game, with a 75% chance of 0 per spot
while True:
    if str(text_map["Start Button"].get()) == "Stop":
        app.step(1)
    app.update_idletasks()
    app.update()