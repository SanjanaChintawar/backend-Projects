import tkinter
from tkinter import messagebox
from tkinter import ttk
import sqlite3

window = tkinter.Tk()
window.title("Hackathon registration form")

frame = tkinter.Frame(window)
frame.pack()


# after submission
def after_submit():
    # t&C accepted or not
    is_accepted = term_bar.get()
    if is_accepted == "not":
        messagebox.showwarning(title="Required Field", message="You must accept the Terms and Conditions to proceed.")
    else:
        # user info
        firstName = first_name_Entry.get()
        lastName = last_name_Entry.get()
        if firstName and lastName:

            title = title_Combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # course info
            academic = aca_status_bar.get()
            collegeName = name_entry.get()
            course = courses_combobox.get()
            semester = semester_spinbox.get()

            if course and collegeName:
                branch = branch_combobox.get()
                # domain info
                domain = choose_combobox.get()
                if domain:
                    skill = skill_entry.get()

                    # hackathon info
                    teamName = team_name_Entry.get()
                    numMembers = num_members_spinbox.get()
                    if teamName:
                        messagebox.showinfo(title="Form Successfully Submitted",
                                            message="Thank you!\n Your registration has been successfully submitted. "
                                                    "We will get back to you soon with further details.")
                        # connect to sqlite
                        conn = sqlite3.connect('DataHackathon.db')
                        table_create_query = '''CREATE TABLE IF NOT EXISTS hackathon_data
                                        (firstName TEXT,lastName TEXT,title TEXT,age INT,nationality TEXT,
                                        academic TEXT,course TEXT,branch TEXT,semester INT,college TEXT,
                                        domain TEXT,skill TEXT,teamName TEXT,numMembers INT)
                                        '''
                        conn.execute(table_create_query)

                        # data insert
                        data_insert_query = '''INSERT INTO hackathon_data(firstName, lastName, title, age, nationality,
                                                academic, course, branch, semester, college, domain, skill, teamName, numMembers)
                                                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
                        data_insert_tuple = (
                            firstName, lastName, title, age, nationality, academic, course, branch, semester,
                            collegeName, domain, skill, teamName, numMembers)

                        cursor = conn.cursor()
                        cursor.execute(data_insert_query, data_insert_tuple)
                        conn.commit()
                        conn.close()

                    else:
                        messagebox.showwarning(title="Required Field",
                                               message="Team name is required.")
                else:
                    messagebox.showwarning(title="Required Field",
                                           message="Choose any domain")

            else:
                messagebox.showwarning(title="Required Field", message="Course and college name is required.")

        else:
            messagebox.showwarning(title="Required Field", message="First and last name of a leader is required.")


# user information

user_info_frame = tkinter.LabelFrame(frame, text="Leader Information *")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name ")
first_name_label.grid(row=0, column=0)
first_name_Entry = tkinter.Entry(user_info_frame)
first_name_Entry.grid(row=1, column=0)
first_name_Entry.focus()

last_name_label = tkinter.Label(user_info_frame, text="Last Name ")
last_name_label.grid(row=0, column=1)
last_name_Entry = tkinter.Entry(user_info_frame)
last_name_Entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title ")
title_label.grid(row=0, column=2)
title_Combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.", "Ms."])
title_Combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age ")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=40)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality ")
nationality_label.grid(row=2, column=1)
nationality_combobox = ttk.Combobox(user_info_frame,
                                    values=["Indian", "American", "Italian", "French", "British", "Australian"])
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# course information

courses_info_frame = tkinter.LabelFrame(frame, text="Course Information *")
courses_info_frame.grid(row=1, column=0, padx=20, pady=10, sticky="news")

academic_label = tkinter.Label(courses_info_frame, text="Academic Status ")
academic_label.grid(row=0, column=0)
aca_status_bar = tkinter.StringVar(value="not pursuing")
academic_check = tkinter.Checkbutton(courses_info_frame, text="Currently pursuing", variable=aca_status_bar,
                                     onvalue="pursuing", offvalue="not pursuing")
academic_check.grid(row=1, column=0)

courses_label = tkinter.Label(courses_info_frame, text="Course name")
courses_label.grid(row=0, column=1)
courses_combobox = ttk.Combobox(courses_info_frame,
                                values=["B-tech", "BCA", "BSC", "BCS", "BE", "Other"])
courses_combobox.grid(row=1, column=1)

branch_label = tkinter.Label(courses_info_frame, text="Branch name(opt)")
branch_label.grid(row=0, column=2)
branch_combobox = ttk.Combobox(courses_info_frame,
                               values=["AI & DS", "CSE", "CSE-AI", "AI & ML", "Mech", "Civil", "DS", "IT"])
branch_combobox.grid(row=1, column=2)

semester_label = tkinter.Label(courses_info_frame, text="Semester(opt)")
semester_label.grid(row=2, column=0)
semester_spinbox = tkinter.Spinbox(courses_info_frame, values=["NA", 1, 2, 3, 4, 5, 6, 7, 8])
semester_spinbox.grid(row=3, column=0)

name_label = tkinter.Label(courses_info_frame, text="College Name")
name_label.grid(row=2, column=1)
name_entry = tkinter.Entry(courses_info_frame)
name_entry.grid(row=3, column=1)

for widget in courses_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Domain choice
domain_info_frame = tkinter.LabelFrame(frame, text="Skills & Domain *")
domain_info_frame.grid(row=2, column=0, padx=20, pady=10, sticky="news")

choose_domain = tkinter.Label(domain_info_frame, text="Choose the Domain")
choose_domain.grid(row=0, column=0)
choose_combobox = ttk.Combobox(domain_info_frame,
                               values=["Web Development", "Android Development", "IOS Development", "Cyber Security",
                                       "Game Development", "Internet and things", "Software Development"])
choose_combobox.grid(row=1, column=0)

skill_label = tkinter.Label(domain_info_frame, text="Programming language known(opt)")
skill_label.grid(row=0, column=1)
skill_entry = tkinter.Entry(domain_info_frame)
skill_entry.grid(row=1, column=1)

for widget in domain_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Hackathon-Specific Information
team_info_frame = tkinter.LabelFrame(frame, text="Hackathon-Specific Information*")
team_info_frame.grid(row=3, column=0, padx=20, pady=10, sticky="news")

team_name_label = tkinter.Label(team_info_frame, text="Team Name")
team_name_label.grid(row=0, column=0)
team_name_Entry = tkinter.Entry(team_info_frame)
team_name_Entry.grid(row=1, column=0)

num_members_label = tkinter.Label(team_info_frame, text="Number of members")
num_members_label.grid(row=0, column=1)
num_members_spinbox = tkinter.Spinbox(team_info_frame, from_=2, to=5)
num_members_spinbox.grid(row=1, column=1)

for widget in team_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms and condition

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions *")
terms_frame.grid(row=4, column=0, sticky="news", padx=20, pady=10)

term_bar = tkinter.StringVar(value="not")

terms_check = tkinter.Checkbutton(terms_frame, text="I accept all the Terms and Conditions.",
                                  font=("Arial", 15, "bold"), variable=term_bar, onvalue="Accepted", offvalue="not")
terms_check.grid(row=0, column=0, padx=10, pady=10)

# submit button
button = tkinter.Button(frame, text="Submit Data", command=after_submit)
button.grid(row=5, column=0, padx=200, pady=15, sticky="news")

window.mainloop()
