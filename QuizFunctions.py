# Functions pertaining to running users quizzes.
import DatabaseFunctions
import customtkinter
from tkinter import messagebox

def submit(chosen_answer, correct_answer, frame):
    if chosen_answer == correct_answer:
        messagebox.showinfo("CORRECT")
    else:
        messagebox.showinfo("WRONG")
    # Destroy currently created radiobuttons in frame. 
    for widget in frame.winfo_children():
        widget_type = str(type(widget))
        print(widget_type)
        if widget_type == "<class 'customtkinter.windows.widgets.ctk_radiobutton.CTkRadioButton'>":
            widget.destroy()
        elif widget_type == "<class 'customtkinter.windows.widgets.ctk_textbox.CTkTextbox'>":
            widget.destroy()

def generate_question(frame):
    question_data = DatabaseFunctions.retrieve_question_data()
    question = question_data[0]
    correct_answer = question_data[1]
    answer_bank = question_data[2]
    question_box = customtkinter.CTkTextbox(frame)
    question_box.grid(row=1, column=0)
    question_box.insert("0.0", question)
    question_box.configure(state="disabled")
    choice_1 = customtkinter.CTkRadioButton(master=frame, text=answer_bank[0], command=lambda: submit(answer_bank[0], correct_answer, frame))
    choice_2 = customtkinter.CTkRadioButton(master=frame, text=answer_bank[1], command=lambda: submit(answer_bank[1], correct_answer, frame))
    choice_3 = customtkinter.CTkRadioButton(master=frame, text=answer_bank[2], command=lambda: submit(answer_bank[2], correct_answer, frame))
    choice_4 = customtkinter.CTkRadioButton(master=frame, text=answer_bank[3], command=lambda: submit(answer_bank[3], correct_answer, frame))
    choice_1.grid()
    choice_2.grid()
    choice_3.grid()
    choice_4.grid()