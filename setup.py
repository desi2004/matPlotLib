import csv
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


# read the data from the CSV file
with open('C:/Users/huami/Dropbox/Trading Journal/Plus500/Real/Trading Record Analysis/Plus500Report_01-12-2008_01-04-2023.csv', 'r') as file:
    #reader = csv.reader(file)
    reader = csv.reader(file, delimiter=',')
    # Initialize an empty array to store the data
    data = []
    data_raw = []
    # Loop through each row in the CSV file and append it to the data array
    for row in reader:
       # str_raw=str(row[0])
       # data_raw=str_raw.split(',')
        data.append(row)
        # print(row)

# create a new window
window = tk.Tk()

# create a Figure object
fig = Figure(figsize=(5, 4), dpi=100)

# add a subplot to the figure
ax = fig.add_subplot(111)

# create a label widget to display the data
data_label = tk.Label(window)

# create a canvas widget
canvas = tk.Canvas(window)

# create a frame widget inside the canvas
frame = tk.Frame(canvas)

# create a vertical scrollbar for the canvas
scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)

# configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# pack the scrollbar to the right side of the window
scrollbar.pack(side="right", fill="y")

# pack the canvas to the left side of the window
canvas.pack(side="left", fill="both", expand=True)

# add the frame to the canvas
canvas.create_window((0, 0), window=frame, anchor="nw")



data = data[1:1000]  # slice rows 1 to 2 (excluding the last index)
data = [row[16] for row in data]  # slice columns 1 to 2 for each row

arr = np.array(data)
arr_str = arr.flatten() # flatten the 2D array to 1D
arr_float = []
for val in arr_str:
    if val:
        arr_float.append(float(val)) # convert non-empty values to int
    else:
        arr_float.append(0) # set empty values to 0
arr_int = np.array(arr_float).reshape(arr.shape)
print(arr_float)


# create some data for the graph
x = np.arange(1, 1000)
y = arr_float

# plot the data on the subplot
ax.plot(x, y)

# update the y-coordinates of the graph
# ax.plot(x, y)

# create a canvas widget to display the graph
canvas = FigureCanvasTkAgg(fig, master=window)

# pack the canvas widget to the window
canvas.get_tk_widget().pack()

# set the text of the label to


# set the text of the label to the CSV data
# data_label.config(text=data)

# add the label widget to the window
#data_label.pack()

# configure the canvas to resize when the frame changes size
#frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

# start the main event loop
window.mainloop()


