import tkinter as tk
from tkinter import ttk, messagebox
import random
from quiz_data import quiz_data
from quiz_data import quiz_data2
from PIL import Image, ImageTk
import os
import sys

#Function to get the path
def resource_path(relative_path):
    base_path = os.path.abspath("images and texts") #Path for images and texts
    return os.path.join(base_path, relative_path)

root_main = tk.Tk()
root_main.title("Käänded")
root_main.geometry("250x200")

def back_to_main(current_window):
    current_window.withdraw() #Hiding the window, but not destroying it
    root_main.deiconify() #Showing the hidden window

#Function for back button
def back_to_previous(current_window, previous_window):
    current_window.withdraw() #Hiding the window, but not destroying it
    previous_window.deiconify() #Showing the hidden window




# List of text filenames for each window
text_files_est = ['test.txt', 'text.txt', 'text_rus.txt']  # Add more filenames as needed

image_params_est = [ [{'file': '14käänet.png', 'coords': (200, 70), 'size': (350, 250)}, {'file': '14käänet2.png', 'coords': (420, 420), 'size': (450, 250)}],
               [{'file': 'tabel_rus.png', 'coords': (50, 300), 'size': (300, 200)}, {'file': 'mitmus.png', 'coords': (420, 300), 'size': (250, 200)}],
               [{'file': 'nimisona.png', 'coords': (50, 300), 'size': (400, 300)}]#, {'file': 'img3_2.png', 'coords': (420, 300), 'size': (350, 250)}]
            ]

text_files_rus = ['text.txt', 'test.txt', 'text_rus.txt']  # Add more filenames as needed

image_params_rus = [ [{'file': '14käänet2.png', 'coords': (200, 70), 'size': (350, 250)}, {'file': '14käänet.png', 'coords': (420, 420), 'size': (450, 250)}],
               [{'file': 'nimisona.png', 'coords': (50, 300), 'size': (300, 200)}, {'file': 'mitmus.png', 'coords': (420, 300), 'size': (250, 200)}],
               [{'file': 'nimisona.png', 'coords': (50, 300), 'size': (400, 300)}]#, {'file': 'img3_2.png', 'coords': (420, 300), 'size': (350, 250)}]
            ]




def create_window(previous_window, index, text_files, image_params):
    if index >= len(text_files):
        return  # If no more text files, stop creating new windows

    previous_window.withdraw()  # Hide the previous window

    new_window = tk.Toplevel(previous_window)
    new_window.title(f"Teooria - Aken {index + 1}")
    new_window.geometry("1000x1000")

    btn_back = ttk.Button(new_window, text="Tagasi", command=lambda: back_to_previous(new_window, previous_window))
    btn_back.place(x=390, y=20, width=110)

    if index < len(text_files) - 1:
        btn_next = ttk.Button(new_window, text="Järgmine", command=lambda: create_window(new_window, index + 1, text_files, image_params))
        btn_next.place(x=500, y=20, width=110)

    # Read and process text from the corresponding file
    with open(resource_path(text_files[index]), encoding='utf-8') as file:
        content = file.read()

    parts = content.split('[[IMG')  # Split the text at markers

    y_position = 50  # Initial y-position for text

    for i, part in enumerate(parts):
        if i == 0:
            label = tk.Label(new_window, text=part.strip(), wraplength=700, justify=tk.LEFT)
            label.place(x=50, y=y_position)
            y_position += 50
        else:
            marker, text = part.split(']]', 1)
            img_index = int(marker) - 1

            # Load and display the image
            img_info = image_params[index][img_index]
            image = Image.open(resource_path(img_info['file']))
            resize_image = image.resize(img_info['size'])  # Resize as needed
            img = ImageTk.PhotoImage(resize_image)

            img_label = tk.Label(new_window, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.place(x=img_info['coords'][0], y=img_info['coords'][1])
            y_position = img_info['coords'][1] + img_info['size'][1] + 50

            # Display the text after the image
            label = tk.Label(new_window, text=text.strip(), wraplength=700, justify=tk.LEFT)
            label.place(x=50, y=y_position)
            y_position += 50




#Function for window where is possible to choose between theory and test
def rus():
    root_main.withdraw() #Hiding the main window, but not destroying it
    gamesc = tk.Toplevel(root_main) #Create a window on top
    gamesc.title("Vene") #New window's name
    gamesc.geometry("250x200") #New window's size

    btn_theory = ttk.Button(gamesc, text="Õppematerjalid", command=lambda: theory_rus(gamesc))
    btn_theory.place(x=70, y=60, width=110)

    btn_test = ttk.Button(gamesc, text="Test", command=lambda: test_rus(gamesc))
    btn_test.place(x=70, y=100, width=110)

    btn_back = ttk.Button(gamesc, text="Tagasi", command=lambda: back_to_main(gamesc))
    btn_back.place(x=70, y=140, width=110)

def est():
    root_main.withdraw() #Hiding the main window, but not destroying it
    gamesc2 = tk.Toplevel(root_main)
    gamesc2.title("Eesti")
    gamesc2.geometry("250x200")

    btn_theory = ttk.Button(gamesc2, text="Õppematerjalid", command=lambda: theory_est(gamesc2)) #Button for moving to the theory window
    btn_theory.place(x=70, y=60, width=110) #Button place

    btn_test = ttk.Button(gamesc2, text="Test", command=lambda: test_est(gamesc2)) #Button to move for a test window
    btn_test.place(x=70, y=100, width=110) #Button place

    btn_back = ttk.Button(gamesc2, text="Tagasi", command=lambda: back_to_main(gamesc2)) #Button to move back
    btn_back.place(x=70, y=140, width=110) #Button place

#Function for a theory window

def theory_rus(gamesc):
    gamesc.withdraw()  # Hide the main window, but not destroy it
    create_window(gamesc, 0, text_files_rus, image_params_rus)

#Function for a test window
def test_rus(gamesc):
    gamesc.withdraw()
    gamesc4 = tk.Toplevel(gamesc)
    gamesc4.title("Test")
    gamesc4.geometry("250x200")

    btn_next = ttk.Button(gamesc4, text="Kõik käänded", command=lambda: all_rus(gamesc4))
    btn_next.place(x=70, y=60, width=110)

    btn_back = ttk.Button(gamesc4, text="Tagasi", command=lambda: back_to_previous(gamesc4, gamesc))
    btn_back.place(x=70, y=100, width=110)


def all_rus(gamesc4):
    gamesc4.withdraw()
    gamesc5 = tk.Toplevel(gamesc4)
    gamesc5.title("Test")
    gamesc5.geometry("600x600")

    #Initializing variables
    score = 0
    current_question = 0
    random.shuffle(quiz_data) #Shuffle the list of questions

    #Time
    sec = 0
    min = 0

    #Function for a timer
    def start_timer():
        nonlocal sec, min
        sec += 1
        if sec == 60:
            sec = 0
            min += 1
        timer_label.config(text=f"{min:02}:{sec:02}")
        gamesc5.after(1000, start_timer)

    #Function to display a question
    def show_question():
        question = quiz_data[current_question]
        qs_label.config(text=question["question"])
        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal")
        feedback_label.config(text="")
        next_btn.config(state="disabled")

    #Function to check the answer
    def check_answer(choice):
        nonlocal score, current_question
        question = quiz_data[current_question]
        selected_choice = choice_btns[choice].cget("text")
        if selected_choice == question["answer"]:
            score += 1
            score_label.config(text="Punktid: {}/{}".format(score, len(quiz_data)))
            feedback_label.config(text="Õige!")
        else:
            feedback_label.config(text="Vale!\nÕige vastus oli: {}".format(question["correct"]))
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    #Function to move to next question
    def next_question():
        nonlocal current_question
        current_question += 1
        if current_question < len(quiz_data):
            show_question()
        else:
            messagebox.showinfo("Test on tehtud!",
                                f"Test on tehtud! Sinu tulemus: {score}/{len(quiz_data)} \n" f"Protsent: {score * 100 / len(quiz_data):.2f}% \n Aeg: {min:02}:{sec:02}")
            gamesc5.destroy()

    #Widgets
    timer_label = tk.Label(gamesc5, text="00:00")
    timer_label.pack(pady=10)
    start_timer()

    qs_label = ttk.Label(gamesc5)
    qs_label.pack(pady=10)


    choice_btns = [] #Choice buttons
    for i in range(4):
        button = ttk.Button(gamesc5, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_btns.append(button)

    feedback_label = ttk.Label(gamesc5) #Feedback
    feedback_label.pack(pady=10)

    score_label = ttk.Label(gamesc5, text="Punktid: 0/{}".format(len(quiz_data))) #Score
    score_label.pack(pady=10)

    next_btn = ttk.Button(gamesc5, text="Edasi", command=next_question, state="disabled") #Button to move forward
    next_btn.pack(pady=10)

    show_question()

    btn_back = ttk.Button(gamesc5, text="Tagasi", command=lambda: back_to_previous(gamesc5, gamesc4)) #Button to move back
    btn_back.place(x=243.5, y=500, width=110)

#Function for a theory window
def theory_est(gamesc2):
    gamesc2.withdraw()
    create_window(gamesc2, 0, text_files_est, image_params_est)

#Function for a test window
def test_est(gamesc2):
    gamesc2.withdraw()
    gamesc7 = tk.Toplevel(gamesc2)
    gamesc7.title("Test")
    gamesc7.geometry("250x200")

    btn_next = ttk.Button(gamesc7, text="Kõik käänded", command=lambda: all_est(gamesc7))
    btn_next.place(x=70, y=60, width=110)

    btn_back = ttk.Button(gamesc7, text="Tagasi", command=lambda: back_to_previous(gamesc7, gamesc2))
    btn_back.place(x=70, y=100, width=110)


def all_est(gamesc7):
    gamesc7.withdraw()
    gamesc8 = tk.Toplevel(gamesc7)
    gamesc8.title("Test")
    gamesc8.geometry("600x600")

    score2 = 0
    current_question2 = 0
    random.shuffle(quiz_data2)

    #selection of random questions
    selected_questions = random.sample(quiz_data2, 10)


    sec = 0
    min = 0

    def start_timer():
        nonlocal sec, min
        sec += 1
        if sec == 60:
            sec = 0
            min += 1
        timer_label.config(text=f"{min:02}:{sec:02}")
        gamesc8.after(1000, start_timer)

    def show_question():
        question = selected_questions[current_question2]

        nm_label.config(text=question["name"])
        qs_label.config(text=question["question"])
        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal")
        feedback_label.config(text="")
        next_btn.config(state="disabled")

        # Question counter
        question_counter_label.config(text=f"Küsimus: {current_question2 + 1} / {len(selected_questions)}")

    def check_answer(choice):
        nonlocal score2, current_question2
        question = selected_questions[current_question2]
        selected_choice = choice_btns[choice].cget("text")
        if selected_choice == question["answer"]:
            score2 += 1
            score_label.config(text="Punktid: {}/{}".format(score2, len(selected_questions)))
            feedback_label.config(text="Õige!")
        else:
            feedback_label.config(text="Vale!\nÕige vastus oli {}".format(question["correct"]))
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    def next_question():
        nonlocal current_question2
        current_question2 += 1
        if current_question2 < len(selected_questions):
            show_question()
        else:
            messagebox.showinfo("Test on tehtud!",
                                f"Test on tehtud! Sinu tulemus: {score2}/{len(selected_questions)} \n" f"Protsent: {score2 * 100 / len(selected_questions):.2f}% \n Aeg: {min:02}:{sec:02}" )
            gamesc8.destroy()

    #Widgets
    timer_label = tk.Label(gamesc8, text="00:00")
    timer_label.pack(pady=10)
    start_timer()

    nm_label = ttk.Label(gamesc8)
    nm_label.pack(pady=10)

    qs_label = ttk.Label(gamesc8)
    qs_label.pack(pady=10)

    choice_btns = []
    for i in range(4):
        button = ttk.Button(gamesc8, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_btns.append(button)

    #Question counter
    question_counter_label = ttk.Label(gamesc8, text=f"Küsimus: {current_question2 + 1} / {len(selected_questions)}")
    question_counter_label.pack(pady=10)

    feedback_label = ttk.Label(gamesc8)
    feedback_label.pack(pady=10)

    score_label = ttk.Label(gamesc8, text="Punktid: 0/{}".format(len(selected_questions)))
    score_label.pack(pady=10)

    next_btn = ttk.Button(gamesc8, text="Edasi", command=next_question, state="disabled")
    next_btn.pack(pady=10)

    show_question()

    btn_back = ttk.Button(gamesc8, text="Tagasi", command=lambda: back_to_previous(gamesc8, gamesc7))
    btn_back.place(x=246.5, y=500, width=110)

btn = ttk.Button(root_main, text="Vene", command=rus)
btn.place(x=70, y=100, width=110)

btn2 = ttk.Button(root_main, text="Eesti", command=est)
btn2.place(x=70, y=60, width=110)

root_main.mainloop() #Cycle end

#