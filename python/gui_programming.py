from tkinter import *

# # this is a GUI module
# # tkinter is an interface to the Tk GUI toolkit

# # Frame is a predefined class in tkinter. It is a container widget which is used to contain other widgets.
# # It works like a container which is responsible for arranging the position of other widgets.
# class Window(Frame):
#     def __init__(self, master = None):
#         Frame.__init__(self, master)
#         self.master = master

# # root is the main window
# # initialize the tkinter window
# root = Tk()

# # object of the frame class
# app = Window(root)

# # set the window title
# root.wm_title("GUI Programming")


# # mainloop() is an infinite loop used to run the application, 
# # wait for an event to occur and process the event as long as the window is not closed
# root.mainloop()

# class Window(Frame):
#     def __init__(self, master = None):
#         Frame.__init__(self, master)
#         self.master = master

#         # widget can take all window
#         self.pack(fill=BOTH, expand=1)

#         # create a button instance and link it to the callback function (exit button)
#         exitButton = Button(self, text="Exit", fg='white', bg='gray', command=self.clickExitButton)

#         # place the button at the top left corner
#         # exitButton.place(x=0, y=0)
#         exitButton.pack(side=LEFT)
    
#     def clickExitButton(self):
#         print("Exit button clicked.")
#         exit()

# root = Tk()

# app = Window(root)

# root.wm_title("Tkinter Button")

# root.geometry("320x200")

# root.mainloop()

# def dowork():
#     print("Hello World!")

# def exit_frame():
#     print("Program exited successfully!")
#     exit()

# root = Tk()
# root.wm_title("Tkinter Test")
# root.geometry('320x200')

# f = Frame(root)
# # pack the frame into the root window
# f.pack()

# b = Button(f, text='Say', command=dowork)
# # pack the button into the frame which is inside the root window.
# b.pack()

# b2 = Button(f, text='Exit', fg='white', bg='gray', command=exit_frame)
# b2.pack()

# root.mainloop()

# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master

#         menu = Menu(self.master)
#         self.master.config(menu=menu)

#         fileMenu = Menu(menu)
#         fileMenu.add_command(label="Item")
#         fileMenu.add_command(label="Exit", command=self.exitProgram)
#         menu.add_cascade(label="File", menu=fileMenu)

#         editMenu = Menu(menu)
#         editMenu.add_command(label="Undo")
#         editMenu.add_command(label="Redo")
#         menu.add_cascade(label="Edit", menu=editMenu)

#         databaseMenu = Menu(menu)
#         databaseMenu.add_command(label="Insert", command=self.insert)
#         databaseMenu.add_command(label="Update", command=self.update)
#         databaseMenu.add_command(label="Create", command=self.create)
#         databaseMenu.add_command(label="Delete", command=self.delete)
#         menu.add_cascade(label="Database", menu=databaseMenu)

#     def exitProgram(self):
#         print("Program exited successfully!")
#         exit()

#     def insert(self):
#         print("Records inserted to database successfully!")
#     def update(self):
#         print("Database record updated successfully!")
#     def create(self):
#         print("Table created in database successfully!")
#     def delete(self):
#         print("Record deleted from database successfully!")

# root = Tk()

# app = Window(root)

# root.wm_title("Menu Window")

# root.mainloop()