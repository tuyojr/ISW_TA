from tkinter import *
import tkinter.messagebox
from crud import Database

class Database_Frame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # initialize the listbox
        self.listbox = Listbox(self)
        self.listbox.place(anchor=CENTER, relx=0.5, rely=0.5, height=400, width=400)

        # Button to insert record at bottom left of frame
        self.insert_button = Button(self, text="INSERT", command=self.insert_record)
        self.insert_button.place(x=100, y=550)

        # Button to select record beside insert button
        self.select_button = Button(self, text="SELECT", command=self.select_record)
        self.select_button.place(x=200, y=550)

        # Button to delete record beside update button
        self.delete_button = Button(self, text="DELETE", command=self.delete_record)
        self.delete_button.place(x=300, y=550)

        # Button to clear the listbox at bottom right of frame before exit
        self.clear_button = Button(self, text="CLEAR", command=self.clear_listbox) 
        self.clear_button.place(x=400, y=550)

        # Button to exit program at bottom right of frame
        self.exit_button = Button(self, text="Exit", command=self.exit_program)
        self.exit_button.place(x=500, y=550)

    def insert_record(self):
        self.name = name_entry.get()
        self.mark = mark_entry.get()
        self.new_record = Database(self.name, int(self.mark))
        self.new_record.collect_user_records()
        self.new_record.insert_records()
        self.listbox.insert(END, self.select_record(self.name))
        tkinter.messagebox.showinfo("Insert", "Record inserted successfully!")
    
    def select_record(self):
        self.name = name_entry.get()
        self.get_record = Database(self.name)
        self.get_record.select_record_by_name(self.name)
        self.listbox.insert(END, self.get_record.select_record_by_name(self.name))
        if self.get_record.select_record_by_name(self.name) == None:
            tkinter.messagebox.showerror("Select", "Record not found!")
        else:
            tkinter.messagebox.showinfo("Select", "Record found!")

    def delete_record(self):
        self.name = name_entry.get()
        self.remove_record = Database(self.name)
        self.listbox.delete(END, self.select_record(self.name))
        self.remove_record.delete_records(self.name)
        tkinter.messagebox.showinfo("Delete", "Record deleted successfully!")

    def clear_listbox(self):
        self.listbox.delete(0, END)

    def exit_program(self):
        exit = tkinter.messagebox.askyesno("Exit", "Do you want to exit?")
        if exit > 0:
            root.destroy()
            return

root = Tk()
root.title("Database")
root.geometry("600x600")

app = Database_Frame(root)

name_label = Label(app, text="name: ")
name_label.pack()

name_entry = Entry(app)
name_entry.pack()

mark_label = Label(app, text="mark: ")
mark_label.pack()

mark_entry = Entry(app)
mark_entry.pack()

root.mainloop()