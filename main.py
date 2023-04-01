import tkinter as tk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# create a new window
window = tk.Tk()

# create a Figure object
fig = Figure(figsize=(5, 4), dpi=100)

# add a subplot to the figure
ax = fig.add_subplot(111)

# create some data for the graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# plot the data on the subplot
ax.plot(x, y)

# create a canvas widget to display the graph
canvas = FigureCanvasTkAgg(fig, master=window)

# pack the canvas widget to the window
canvas.get_tk_widget().pack()

# start the main event loop
window.mainloop()





