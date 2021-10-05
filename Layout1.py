from tkinter import *
from tpr_1 import array2
from tpr_1 import best_option
name_method = ["Valds", "Laplas", "Gurvic", "Baes"]

class Table:
    def __init__(self, root):
        for i in range(len(best_option)):
            self.e = Entry(root, width=10, fg='blue',
                                   font=('Arial',16,'bold'), justify=CENTER)

            self.e.grid
            self.e.grid(row=0, column=3+i)
            self.e.insert(END, name_method[i])

        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=10, fg='blue',
                               font=('Arial',16,'bold'))

                self.e.grid

                self.e.grid(row=i+1, column=j)
                self.e.insert(END, array2[i][j])
        for i in range(len(best_option)):
            self.e = Entry(root, width=10, fg='blue',
                                   font=('Arial',16,'bold'), justify=CENTER)

            self.e.grid
            self.e.grid(row=6, column=3+i)
            self.e.insert(END, best_option[i])


total_rows = len(array2)
total_columns = len(array2[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()
