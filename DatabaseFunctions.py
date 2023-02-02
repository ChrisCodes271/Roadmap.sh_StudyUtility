#Functions involved with database manipulation. This program utilizes SQLite3 for database management.

import sqlite3
from sqlite3 import Error
import os
from tkinter import StringVar
from customtkinter import CTkLabel
from customtkinter import CTkCheckBox
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import random

# Establish global variables for current test bank (db) and category (table), and set it to an empty string.
global current_db
global current_db_readable
global current_table
current_db = ""
current_table = ""


# Databases will act as "Question Banks" for user

# Select current database
def select_current_database():
    global current_db
    global current_db_readable
    current_db = os.path.basename(filedialog.askopenfilename(title="Select a Question Bank", filetypes=(("Database Files", "*.db"),)))

    

# Create database 
def create_database():
    try:
        conn = None
        user_bank_name = simpledialog.askstring(title="Name Question Bank", prompt="Please enter a topic for your new question bank.")
        conn = sqlite3.connect(user_bank_name.replace(" ", "")+"_Question_Bank"+'.db')
    except Error as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))
    finally:
        if conn:
            conn.close

# Delete database
def delete_database():
    try:
        if current_db == "":
            select_current_database()
        user_warning = messagebox.askquestion(title="Delete Question Bank?",message="You are about to delete " + current_db + "do you wish to continue?",icon='warning')
        if user_warning == 'yes':
            os.remove(current_db)
    except Exception as e:
            messagebox.showerror(title="An Error Occured", message=str(e))

# Tables will function as "topics", or "question categories" for the user. 

check_var = StringVar("on")

def checkbox_event():
    print(check_var.get())
    print(type(check_var))

# Display all tables
def display_all_tables(frame):
    try:
        if current_db == "":
            select_current_database()
        conn = sqlite3.connect(current_db)
        cursor = conn.cursor()
        database_data= cursor.execute("SELECT * FROM sqlite_master WHERE type='table';").fetchall()
        user_category_prompt = CTkLabel(frame, text=' Here is a list of categories in the ' + current_db + " ") 
        user_category_prompt.pack()
        for item in database_data:
            table_display = CTkCheckBox(frame, text=item[1], command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
            table_display.pack()
    except Exception as e:
        print(e)

# Select current table
def select_current_table():
    pass


def create_table():
    try:
        if current_db == "":
            select_current_database()
        conn = sqlite3.connect(current_db)
        cursor = conn.cursor()
        user_table_name = simpledialog.askstring(title="Create Question Category", prompt="Please enter a category name")
        cursor.execute("CREATE TABLE " + user_table_name + "(EntryID INTEGER PRIMARY KEY, Question varchar(255), Answer varchar(255));")
    except Error as e:
        messagebox.showerror(title="An Error Occured", message=str(e))
    finally:
        conn.close()

# Delete current Question Bank table
def delete_table():  
    try:
        conn = sqlite3.connect(current_db)
        cursor = conn.cursor()
        cursor.execute('DROP TABLE ' + current_table)
        conn.close()
    
    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))

# Generate new entry into the Question Bank table. 
def new_quizbank_entry():
    try:
        user_question = simpledialog.askstring(title='Add Question', prompt='Please enter the question you wish to store in your quiz bank.')
        user_answer = simpledialog.askstring(title='Add Answer', prompt='Please enter the correct answer to store in your quiz bank.')

        user_entry = [user_question, user_answer]
        conn = sqlite3.connect(current_db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO QUESTION_BANK (Question, Answer) VALUES (?,?);", user_entry)
        conn.commit()
        conn.close()

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))

# Delete entry from Question Bank.
def delete_quizbank_entry():
    try:
        entry_id = simpledialog.askstring(title='Entry Number', prompt='What entry number would you like to delete?')
        conn = sqlite3.connect('QuestionBank.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM QUESTION_BANK WHERE EntryID = ?;", entry_id)
        conn.commit()
        conn.close()

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))

# Pull new question data.
def retrieve_question_data():
    conn = sqlite3.connect('QuestionBank.db')
    cursor = conn.cursor()
    random_question_pool = cursor.execute("SELECT Question, Answer FROM QUESTION_BANK ORDER BY RANDOM() LIMIT 4;").fetchall()
    cursor.close
    chosen_question = random_question_pool[0][0]
    correct_answer = random_question_pool[0][1]
    answer_2 = random_question_pool[1][1]
    answer_3 = random_question_pool[2][1]
    answer_4 = random_question_pool[3][1]
    answer_bank = [correct_answer, answer_2, answer_3, answer_4]
    random.shuffle(answer_bank)
    return chosen_question, correct_answer, answer_bank