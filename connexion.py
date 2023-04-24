from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import mysql.connector as MC
import hashlib
import tkinter.messagebox as messagebox


# configurations
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")
window = Tk()
window.title("Connexion")
window.geometry("619x418")
window.configure(bg="#FFFFFF")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
# configurations

# fonctions


def connexion():
    conn = MC.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )
    cursor = conn.cursor()
    username = entry_1.get()
    password = entry_2.get()
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    query = "SELECT * FROM users WHERE nom=%s AND mot_de_passe=%s"
    cursor.execute(query, (username, hashed_password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result is None:
        messagebox.showerror("Erreur authentification",
                             "Nom d'utilisateur ou mot de passe incorrect.")
        return False
    else:
        window.destroy()
        import menu
        return True
button_image_1 = None
def test():
    global button_image_1
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=test,
        relief="flat"
    )
    button_1.place(
        x=39.0,
        y=332.0,
        width=145.0,
        height=41.0
    )
# fonctions


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=418,
    width=619,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    309.0,
    209.0,
    image=image_image_1
)

canvas.create_rectangle(
    309.0,
    0.0,
    619.0,
    418.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    463.0,
    170.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C3CEF6",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=367.0,
    y=152.0,
    width=192.0,
    height=35.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    463.0,
    260.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C3CEF6",
    fg="#000716",
    show="°",
    highlightthickness=0
)
entry_2.place(
    x=367.0,
    y=242.0,
    width=192.0,
    height=35.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=test,
    relief="flat"
)
button_1.place(
    x=390.0,
    y=332.0,
    width=145.0,
    height=41.0
)

canvas.create_text(
    352.0,
    35.0,
    anchor="nw",
    text="Bienvenue, veuillez",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    352.0,
    62.0,
    anchor="nw",
    text="vous connecter",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    357.0,
    132.0,
    anchor="nw",
    text="nom d’utilisateur",
    fill="#000000",
    font=("Inter Bold", 15 * -1)
)

# canvas.create_text(
#     357.0,
#     222.0,
#     anchor="nw",
#     text="mot de passe",
#     fill="#000000",
#     font=("Inter Bold", 15 * -1)
# )


window.resizable(False, False)
window.mainloop()
