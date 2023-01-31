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
#Question Bank Menu Dropdown
question_bank_menu = Menu(menu_bar, tearoff=0, background='blue', foreground='black', activebackground='black', activeforeground='blue')
question_bank_menu.add_command(label="Open Question Bank", command=DatabaseFunctions.select_current_database)
question_bank_menu.add_command(label="New Question Bank", command=DatabaseFunctions.create_database)
question_bank_menu.add_command(label="Delete Current Question Bank",command=DatabaseFunctions.delete_database)
#Question Category Menu Dropdown
question_category_menu = Menu(menu_bar, tearoff=0, background='blue', foreground='black', activebackground='black', activeforeground='blue')
question_category_menu.add_command(label="Add Category to Question Bank", command=DatabaseFunctions.create_table)
question_category_menu.add_command(label="Remove Category from Question Bank", command=DatabaseFunctions.delete_quizbank_entry)
question_category_menu.add_command(label="View Categories in Current Question Bank", command=lambda: DatabaseFunctions.display_all_tables(center_frame))
#Add or Remove Question Menu Dropdown
question_menu = Menu(menu_bar, tearoff=0, background='blue', foreground='black', activebackground='black', activeforeground='blue')
question_menu.add_command(label="Add Question")
question_menu.add_command(label="Remove Question")
question_menu.add_command(label="View Questions in Current Category")
#Menu Bar Cascade Settings
menu_bar.add_cascade(label="Test Bank",menu=question_bank_menu)
menu_bar.add_cascade(label="Categories",menu=question_category_menu)
menu_bar.add_cascade(label="Questions",menu=question_menu)

# New Quiz button
question_button = customtkinter.CTkButton(master=button_frame, text="Ask a Random Question!", command=lambda: QuizFunctions.generate_question(button_frame))
question_button.grid(row=0, column=0)

root.config(menu=menu_bar)
root.mainloop()