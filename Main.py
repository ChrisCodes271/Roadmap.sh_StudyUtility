from tkinter import *
import customtkinter
import QuizFunctions
import DatabaseFunctions

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Globally tracked variables for user progress. 
question_tally = 0
correct_answer_tally = 0

# Root window setup
root = customtkinter.CTk()
root.geometry(f"{800}x{800}")
root.title("Roadmap.sh Study Utility")

# Create two frames. One center frame for user to interface with, the other for buttons / options to run quizzes.
center_frame= Frame(master=root, width=300, height=300, bg='grey')
center_frame.place(relx = 0.5, rely = 0.5, anchor= CENTER)

button_frame  =  Frame(master=root,  width=300,  height=100,  bg='grey')
button_frame.place(x= 315, y= 10)

# Menu bar that will be used to manage test-banks
menu_bar = Menu(root, background='blue', foreground='black', activebackground='black', activeforeground='blue')
testbank_menu = Menu(menu_bar, tearoff=0, background='blue', foreground='black', activebackground='black', activeforeground='blue')
testbank_menu.add_command(label="New Test Bank", command=DatabaseFunctions.create_table)
testbank_menu.add_command(label="Delete Test Bank", command=DatabaseFunctions.delete_table)
testbank_menu.add_command(label="Add to test bank", command=DatabaseFunctions.new_quizbank_entry)
testbank_menu.add_command(label="Remove from test bank", command=DatabaseFunctions.delete_quizbank_entry)
menu_bar.add_cascade(label="Test Bank",menu=testbank_menu)

# New Quiz button
question_button = customtkinter.CTkButton(master=button_frame, text="Ask a Random Question!", command=lambda: QuizFunctions.generate_question(button_frame))
question_button.grid(row=0, column=0)

root.config(menu=menu_bar)
root.mainloop()