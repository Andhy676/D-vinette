import random
from tkinter import *

# Create a window
window = Tk()

# Window settings
window.title("Dévinette")
window.geometry("480x480")

# MAIN PROGRAMM
# create the mystery number
mystery_number = random.randint(0, 9)

# Add the first text
welcome = Label(window, text="Dévine le nombre entre 1 et 10", font=("Courrier", 25))
welcome.pack()

# Create an input
user_number_entry = Entry(window, font=("Courrier", 25), width=20)
user_number_entry.pack(pady=20)


def verify_number():    
    # Get the user number
    user_number = int(user_number_entry.get())

    # Verify the answer
    if user_number == mystery_number:
        new = "Bravo"
        Label.config(text=new)
    elif user_number >= mystery_number:
        new = "Bravo"
        Label.config(text=new)
    elif user_number <= mystery_number:
        new = "Bravo"
        Label.config(text=new)

# Create a button
verify_button = Button(window, text="Vérifier", font=("Courirer", 20), command=verify_number)
verify_button.pack()

#Create a label to display the result
answer = Label(window, text="Entrer un chiffre entre 1 et 9")
answer.pack() 

# Load the window
window.mainloop()
