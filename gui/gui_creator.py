import tkinter
from tkinter import *
import os
from tkinter import messagebox
from game_reader.ReadAndLogic import LogicCreator


class CreateGui(object):

    def __init__(self):
        self.logic_creator = LogicCreator()
        self.dictionary_boxes = self.logic_creator.compute_excel_logic()
        self.ico_image = os.path.join(os.getcwd(), "images/image_math.ico")
        # will store the numbers needed in this list
        self.list_numbers = list()
        self.dict_boxes = dict()
        self.index_boxes = 1
        self.list_operations = [":", "*", "+", "-", "="]
        self.list_entries_numbers = []
        self.list_used_numbers = []
        self.labels_numbers_list = []

    def check_input(self):
        for entry in self.list_entries_numbers:
            if entry.get():
                button_check["state"] = tkinter.NORMAL
                break
            # we should have a logic in the list that only one button should be active as per time
            else:
                button_check["state"] = tkinter.DISABLED

    def check_value(self):
        self.check_input()
        # check if only one entry is completed
        counter_entries = 0
        typed_number = ""
        for entry in self.list_entries_numbers:
            if entry.get():
                counter_entries += 1
                typed_number = entry.get()
        print(typed_number)
        if (counter_entries > 1 and not typed_number.isnumeric()) or (
                counter_entries > 1 and int(typed_number) not in self.list_used_numbers):
            messagebox.showinfo("VALIDATE JUST ONE ENTRY",
                                "Please check just one entry per time and also ensure it is a number!")
            return
        '''
        1. value not from the list box
        '''
        for entry in self.list_entries_numbers:
            if entry.get():
                if not entry.get().isnumeric() or (
                        int(entry.get()) not in self.list_numbers and int(entry.get()) not in self.list_used_numbers):
                    messagebox.showerror("NOT A VALID NUMBER",
                                         message="Not a valid number! Please check the the allowed numbers from below")
                    return

        '''
        2 value already entered in another place and not valid anymore
        '''
        for entry in self.list_entries_numbers:
            if entry.get():
                if int(entry.get()) not in self.list_numbers and int(entry.get()) in self.list_used_numbers:
                    messagebox.showerror("NUMBER ALREADY USED",
                                         message="This number has been used, but it is not present anymore")
        '''
        3. value is not the correct one
        '''
        for entry in self.list_entries_numbers:
            if entry.get():
                if int(entry.get()) in self.list_numbers:
                    entry_string = str(entry)
                    entry_number_string = self.logic_creator.extract_entry_number(entry_string)
                    if entry.get() != str(self.dictionary_boxes[int(entry_number_string)]):
                        messagebox.showerror("INCORRECT VALUE", message="This number is somewhere else")
                        return
                    else:
                        '''
                       4. value is the correct one
                        '''
                        # make the entry green that is correct
                        # add number in new list, delete from original list and delete entry for recheck
                        self.list_used_numbers.append(int(entry.get()))
                        self.list_numbers.remove(int(entry.get()))
                        self.dict_boxes[int(entry_number_string)]["text"] = entry.get()
                        self.dict_boxes[int(entry_number_string)]["state"] = tkinter.DISABLED
                        self.dict_boxes[int(entry_number_string)].config(disabledbackground="#23932d")
                        # remake the label - travers through label till we find that the value matches our entry value
                        for label in self.labels_numbers_list:
                            if label["text"] == entry.get():
                                label.after(1000, label.destroy())
                                # remove from label_list
                                self.labels_numbers_list.remove(label)
                                # to ensure just one value deleted if we have numbers that repeat
                                break
                        self.list_entries_numbers.remove(entry)
        # Present a message when all the entries are completed
        if len(self.list_numbers) == 0:
            messagebox.showinfo(title="GAME COMPLETED", message="You have finished the game")
            # create a frame and put it in the label frame
            label_winner = Label(label_frame_numbers, text="CONGRATULATIONS! YOU COMPLETED THE GAME", justify="center",
                               font=("Helvetica", 18, "bold"), cursor="trek", fg="#37d345", bg="#b7cb83")
            label_winner.grid(row=0, column=1)
            button_check["state"] = tkinter.DISABLED

    def create_game(self, window):
        global button_check
        global label_frame_numbers
        # create big title
        label_title = Label(window, text="MATH GAME! GET THE NUMBERS IN PLACE!", bg="#e7ecbb",
                            font=("Comic Sans Ms", 18, "bold"), fg="#4e8cc8")
        label_title.place(x=350, y=100)
        # create entries
        print(self.dictionary_boxes)
        print(len(self.dictionary_boxes))
        start_value_x = 150
        start_value_y = 250
        x_offset = 125

        for box in self.dictionary_boxes:
            # we do this here to ensure that we have first modified the start values and then we put the entry on the screen
            # the method first done it doesn't work probably due to the fact that we create the widget and then update the values??
            if (self.index_boxes - 1) % 8 == 0 and self.index_boxes != 1:  # Check row break
                start_value_x = 150
                start_value_y += 50

            if self.dictionary_boxes[box] == "x":
                # Create disabled entry with grey background
                dict_variable_creator = {}
                box_name = "Box" + str(self.index_boxes)
                dict_variable_creator[box_name] = Entry(window, width=6, justify="center",
                                                        font=("Helvetica", 30, "bold"),
                                                        cursor="star", bg="#7e8079",
                                                        state=tkinter.DISABLED, fg="#e71212")
                self.dict_boxes.update({self.index_boxes: dict_variable_creator[box_name]})
                dict_variable_creator[box_name].place(x=start_value_x, y=start_value_y)
                start_value_x += x_offset

            elif self.dictionary_boxes[box] in self.list_operations:
                # Create entry for operations
                dict_variable_creator = {}
                box_name = "Box" + str(self.index_boxes)
                entry_text = StringVar()
                dict_variable_creator[box_name] = Entry(window, width=6, justify="center",
                                                        font=("Helvetica", 30, "bold"),
                                                        cursor="star", bg="#7e8079",
                                                        fg="#e71212", textvariable=entry_text)
                self.dict_boxes.update({self.index_boxes: dict_variable_creator[box_name]})
                entry_text.set(self.dictionary_boxes[box])
                dict_variable_creator[box_name].place(x=start_value_x, y=start_value_y)
                start_value_x += x_offset

            else:
                # Create enabled entry for input
                dict_variable_creator = {}
                box_name = "Box" + str(self.index_boxes)
                # create a stringvar to keep track of values
                dict_variable_creator[box_name] = Entry(window, width=6, justify="center",
                                                        font=("Helvetica", 30, "bold"),
                                                        cursor="star", bg="#9fe8dd",
                                                        fg="#e71212")
                self.dict_boxes.update({self.index_boxes: dict_variable_creator[box_name]})
                self.list_entries_numbers.append(dict_variable_creator[box_name])
                dict_variable_creator[box_name].place(x=start_value_x, y=start_value_y)
                start_value_x += x_offset

            self.index_boxes += 1
        # create a label frame and put all the needed numbers
        label_frame_numbers = LabelFrame(window, fg="#07111c", bg="#b7cb83", font=("Helvetica", 16, "bold"), bd=8,
                                         cursor="target", width=550, height=100, labelanchor="n", text="WANTED NUMBERS",
                                         relief=tkinter.GROOVE)
        label_frame_numbers.place(x=350, y=650)
        '''
        need to create a logic to put all numbers as labels automtically
        create some global variables based on the dictionary and check where we have numbers
        '''
        for entry in self.dictionary_boxes:
            if isinstance(self.dictionary_boxes[entry], int):
                self.list_numbers.append(self.dictionary_boxes[entry])
        # create number of globals
        index_column = 1
        for number in self.list_numbers:
            label_name = "Label" + str(number)
            globals()[label_name] = label_name
            label_name = Label(label_frame_numbers, text=str(number), justify="center",
                               font=("Helvetica", 18, "bold"),
                               cursor="trek", fg="#433950", bg="#b7cb83")
            self.labels_numbers_list.append(label_name)
            label_name.grid(row=0, column=index_column, padx=20)
            index_column += 1
        # create button for check
        button_check = Button(label_frame_numbers, text="CHECK", foreground="#e1fdff", bg="#20123a",
                              padx=5, pady=5, font=("Georgia", "9", "bold"), command=lambda: self.check_value(),
                              bd=11, state=tkinter.DISABLED)
        button_check.grid(row=0, column=0, padx=20)
        for entry in self.list_entries_numbers:
            entry.bind("<KeyRelease>", lambda e: self.check_input())  # check if a key is released

    def create_main_gui(self):
        root = Tk()
        root.geometry("1280x960")
        root.iconbitmap(self.ico_image)
        root.title("MATH GAME")
        self.create_game(root)
        root["bg"] = "#e7ecbb"
        root.mainloop()
