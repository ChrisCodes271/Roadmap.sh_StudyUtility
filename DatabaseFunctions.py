#Functions involved with database manipulation. This program utilizes SQLite3 for database management.

import sqlite3
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import random

# Create database if one is not available, then populate Question Bank table.
def create_table():
    try:
        conn = sqlite3.connect('QuestionBank.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE QUESTION_BANK (''EntryID INTEGER PRIMARY KEY,''Question varchar(255),''Answer varchar(255)'');')
        conn.close()

    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))

# Delete current Question Bank table
def delete_table():  
    try:
        conn = sqlite3.connect('QuestionBank.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE QUESTION_BANK')
        conn.close()
    
    except Exception as e:
        messagebox.showerror(title="An Error Occurred", message=str(e))

# Generate new entry into the Question Bank table. 
def new_quizbank_entry():
    try:
        user_question = simpledialog.askstring(title='Add Question', prompt='Please enter the question you wish to store in your quiz bank.')
        user_answer = simpledialog.askstring(title='Add Answer', prompt='Please enter the correct answer to store in your quiz bank.')

        user_entry = [user_question, user_answer]
        conn = sqlite3.connect('QuestionBank.db')
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