import tkinter as tk
from tkinter import ttk, messagebox
import random
from quiz_data import quiz_data
from quiz_data import quiz_data2
from PIL import Image, ImageTk
import os

#Function to get the path
def resource_path(relative_path):
    base_path = os.path.abspath("images and texts") #Path for images and texts
    return os.path.join(base_path, relative_path)

root_main = tk.Tk()
root_main.title("Käänded")
root_main.geometry("250x200+100+100")

global_font = ("Times New Roman", 13)
root_main.option_add("*Font", global_font)

button_font = ("Times New Roman", 13)
root_main.option_add("*TButton.Font", button_font)

def back_to_main(current_window):
    current_window.withdraw() #Hiding the window, but not destroying it
    root_main.deiconify() #Showing the hidden window

#Function for back button
def back_to_previous(current_window, previous_window):
    current_window.withdraw() #Hiding the window, but not destroying it
    previous_window.deiconify() #Showing the hidden window

# List of text filenames for each window
text_files_est = ['test.txt', 'text.txt', 'text1_rus.txt']  # Add more filenames as needed

image_params_est = [ [{'file': '14käänet.png', 'size': (350, 250)}, {'file': '14käänet2.png', 'size': (450, 250)}],
               [{'file': 'tabel1_rus.png', 'size': (300, 200)}, {'file': 'mitmus.png', 'size': (250, 200)}],
               [{'file': 'sugu_rus.png', 'size': (400, 300)}]#, {'file': 'img3_2.png', 'coords': (420, 300), 'size': (350, 250)}]
            ]

text_files_rus = ['text1_rus.txt', 'text2_rus.txt', 'text3_rus.txt', 'text4_rus.txt', 'text5_rus.txt', 'text6_rus.txt']  # Add more filenames as needed

image_params_rus = ([ [{'file': 'tabel1.1_rus.png', 'size': (720, 620)}, {'file': 'sugu_rus.png', 'size': (620, 420)}, {'file': 'mitmus_rus.jpg', 'coords': (50, 920), 'size': (430, 320)}],
               [{'file': 'gen1_rus.png', 'size': (850, 310)}, {'file': 'gen2_rus.png', 'size': (850, 792)}, {'file': 'gen3_rus.jpg', 'size': (650, 800)}],
               [{'file': 'dat1_rus.png', 'size': (850, 310)}, {'file': 'dat2_rus.png', 'size': (869, 276)}, {'file': 'dat3_rus.jpg', 'size': (850, 341)}],
               [{'file': 'acc1_rus.png', 'size': (850, 337)}, {'file': 'acc2_rus.png', 'size': (850, 300)},{'file': 'acc3_rus.jpg', 'size': (850, 510)},{'file': 'acc4_rus.jpg', 'size': (350, 581)} ],
               [{'file': 'ins1_rus.png', 'size': (850, 337)}, {'file': 'ins2_rus.png', 'size': (850, 250)},{'file': 'ins3_rus.jpg', 'size': (850, 380)}],
               [{'file': 'pre1_rus.png', 'size': (850, 500)}, {'file': 'pre2_rus.png', 'size': (850, 130)},{'file': 'pre3_rus.jpg', 'size': (587, 840)}, {'file': 'pre4_rus.jpg', 'size': (678, 960)}, {'file': 'pre5_rus.jpg', 'size': (850, 300)}, {'file': 'pre6_rus.jpg', 'size': (382, 1024)}]
                ])

def create_window(previous_window, index, text_files, image_params):
    if index >= len(text_files):
        return  # If no more text files, stop creating new windows

    previous_window.withdraw()  # Hide the previous window

    new_window = tk.Toplevel(previous_window)
    new_window.title(f"Teooria - Aken {index + 1}")
    new_window.geometry("1000x800+0+0")

    btn_back = ttk.Button(new_window, text="Tagasi", command=lambda: back_to_previous(new_window, previous_window))
    btn_back.place(x=390, y=20, width=110)

    if index < len(text_files) - 1:
        btn_next = ttk.Button(new_window, text="Edasi", command=lambda: create_window(new_window, index + 1, text_files, image_params))
        btn_next.place(x=500, y=20, width=110)

    frame = ttk.Frame(new_window)
    frame.place(x=20, y=50, width=900, height=700)

    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def bind_mouse_wheel(event):
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    new_window.bind("<Map>", bind_mouse_wheel)  # Bind mouse wheel event when window is shown again

    with open(resource_path(text_files[index]), encoding='utf-8') as file:
        content = file.read()

    parts = content.split('[[IMG')  # Split the text at markers

   # text_font = ("Arial", 14)

    for i, part in enumerate(parts):
        if i == 0:
            label = tk.Label(scrollable_frame, text=part.strip(), wraplength=700, justify=tk.LEFT)#, font=text_font)
            label.pack(anchor="w", pady=10)
        else:
            marker, text = part.split(']]', 1)
            img_index = int(marker) - 1

            # Load and display the image
            if img_index < len(image_params[index]):  # Check if img_index is within range
                img_info = image_params[index][img_index]
                image = Image.open(resource_path(img_info['file']))
                resize_image = image.resize(img_info['size'])  # Resize as needed
                img = ImageTk.PhotoImage(resize_image)

                img_label = tk.Label(scrollable_frame, image=img)
                img_label.image = img  # Keep a reference to avoid garbage collection
                img_label.pack(anchor="w", pady=10)

            # Display the text after the image
            label = tk.Label(scrollable_frame, text=text.strip(), wraplength=900, justify=tk.LEFT)#, font=text_font)
            label.pack(anchor="w", pady=10)

#Function for window where is possible to choose between theory and test
def rus():
    root_main.withdraw() #Hiding the main window, but not destroying it
    gamesc = tk.Toplevel(root_main) #Create a window on top
    gamesc.title("Vene") #New window's name
    gamesc.geometry("250x200+100+100") #New window's size

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
    gamesc2.geometry("250x200+100+100")

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
    gamesc4.geometry("250x200+100+100")

    btn_next = ttk.Button(gamesc4, text="Kõik käänded", command=lambda: all_rus(gamesc4))
    btn_next.place(x=70, y=60, width=110)

    btn_back = ttk.Button(gamesc4, text="Tagasi", command=lambda: back_to_previous(gamesc4, gamesc))
    btn_back.place(x=70, y=100, width=110)


def all_rus(gamesc4):
    gamesc4.withdraw()
    gamesc5 = tk.Toplevel(gamesc4)
    gamesc5.title("Test")
    gamesc5.geometry("1000x800+100+100")

    #Initializing variables
    score = 0
    current_question = 0
    random.shuffle(quiz_data) #Shuffle the list of questions

    # selection of random questions
    selected_questions = random.sample(quiz_data, 10)

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
        question = selected_questions[current_question]

        nm_label.config(text=question["name"])
        qs_label.config(text=question["question"])
        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal")
        feedback_label.config(text="")
        next_btn.config(state="disabled")

        # Question counter
        question_counter_label.config(text=f"Küsimus: {current_question + 1} / {len(selected_questions)}")

    #Function to check the answer
    def check_answer(choice):
        nonlocal score, current_question
        question = selected_questions[current_question]
        selected_choice = choice_btns[choice].cget("text")
        if selected_choice == question["answer"]:
            score += 1
            score_label.config(text="Punktid: {}/{}".format(score, len(selected_questions)))
            feedback_label.config(text="Õige!")
        else:
            feedback_label.config(text="Vale!\nÕige vastus oli {}".format(question["correct"]))
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    #Function to move to next question
    def next_question():
        nonlocal current_question
        current_question += 1
        if current_question < len(selected_questions):
            show_question()
        else:
            messagebox.showinfo("Test on tehtud!",
                                f"Test on tehtud! Sinu tulemus: {score}/{len(selected_questions)} \n" f"Protsent: {score * 100 / len(selected_questions):.2f}% \n Aeg: {min:02}:{sec:02}")
            gamesc5.destroy()

    #Widgets
    timer_label = tk.Label(gamesc5, text="00:00")
    timer_label.pack(pady=10)
    start_timer()

    nm_label = ttk.Label(gamesc5)
    nm_label.pack(pady=10)

    qs_label = ttk.Label(gamesc5)
    qs_label.pack(pady=10)

    choice_btns = [] #Choice buttons
    for i in range(4):
        button = ttk.Button(gamesc5, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_btns.append(button)

    # Question counter
    question_counter_label = ttk.Label(gamesc5, text=f"Küsimus: {current_question + 1} / {len(selected_questions)}")
    question_counter_label.pack(pady=10)

    feedback_label = ttk.Label(gamesc5) #Feedback
    feedback_label.pack(pady=10)

    score_label = ttk.Label(gamesc5, text="Punktid: 0/{}".format(len(quiz_data))) #Score
    score_label.pack(pady=10)

    next_btn = ttk.Button(gamesc5, text="Edasi", command=next_question, state="disabled") #Button to move forward
    next_btn.pack(pady=10)

    show_question()

    btn_back = ttk.Button(gamesc5, text="Tagasi", command=lambda: back_to_previous(gamesc5, gamesc4)) #Button to move back
    btn_back.place(x=445, y=500, width=110)

#Function for a theory window
def theory_est(gamesc2):
    gamesc2.withdraw()
    create_window(gamesc2, 0, text_files_est, image_params_est)

#Function for a test window
def test_est(gamesc2):
    gamesc2.withdraw()
    gamesc7 = tk.Toplevel(gamesc2)
    gamesc7.title("Test")
    gamesc7.geometry("250x200+100+100")

    btn_next = ttk.Button(gamesc7, text="Kõik käänded", command=lambda: all_est(gamesc7))
    btn_next.place(x=70, y=60, width=110)

    btn_back = ttk.Button(gamesc7, text="Tagasi", command=lambda: back_to_previous(gamesc7, gamesc2))
    btn_back.place(x=70, y=100, width=110)


def all_est(gamesc7):
    gamesc7.withdraw()
    gamesc8 = tk.Toplevel(gamesc7)
    gamesc8.title("Test")
    gamesc8.geometry("1000x800+100+100")

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
    btn_back.place(x=445, y=500, width=110)

btn = ttk.Button(root_main, text="Vene", command=rus)
btn.place(x=70, y=100, width=110)

btn2 = ttk.Button(root_main, text="Eesti", command=est)
btn2.place(x=70, y=60, width=110)

root_main.mainloop() #Cycle end
