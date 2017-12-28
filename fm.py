from Tkinter import *
import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    
root=Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12") 
#padding is used to add extra space between the widgets
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet=StringVar()
meters=StringVar()

feet_entry=ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

#the statements below declares all the labels with specific grid positions.
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#the statement below is used to do padding in the vertical as well as horizontal axis for all the child widgets of the parent mainframe.
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus() #focus function is used so as to place the cursor automtically in the feet entry widget.

#the statement below tells if the user presses an Enter Key anywhere within the root window, it should Calculate the result, i.e. same as when user pressed the Calculate button. 
root.bind('<Return>', calculate)

#the statement below is required to run the program.
root.mainloop()

