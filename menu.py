from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from subprocess import call
import tkinter as tk
import mysql.connector


# configurations
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame1")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()
window.title("INPTIC - Gestionnaire études")
window.geometry("1500x750")
window.configure(bg="#FFFFFF")
# configurations

# fonctions
def afficherEtudiant():
    frame_etudiant =  tk.Frame(window)
    frame_etudiant.place(x=400, y=150, width=1120, height=500)

    table = ttk.Treeview(frame_etudiant, columns= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), height= 11, show = "headings")
    table.place(x = 0, y = 0, width = 1120, height=500)

    table.heading(1, text="ID")
    table.heading(2, text="Nom")
    table.heading(3, text="Prenom")
    table.heading(4, text="Email")
    table.heading(5, text="Tel")
    table.heading(6, text="Sexe")
    table.heading(7, text="Numero Urgence 1")
    table.heading(8, text="Numero Urgence 2")
    table.heading(9, text="Classe")
    table.heading(10, text="Date Naissance")
    table.heading(11, text="Lieu Naissance")

    table.column(1, width = 5)
    table.column(2, width = 50)
    table.column(3, width = 50)
    table.column(4, width = 80)
    table.column(5, width = 60)
    table.column(6, width = 10)
    table.column(7, width = 30)
    table.column(8, width = 50)
    table.column(9, width = 30)
    table.column(10, width = 50)
    table.column(11, width = 70)

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="inptic")
    meConnect = maBase.cursor()
    meConnect.execute("select * from etudiant")
    resultat = meConnect.fetchall()
    # for row in resultat:
    #     table.insert('', 'end', value=row)
    table.tag_configure('evenrow', background='#d1faff')
    table.tag_configure('oddrow', background='#fff9d4')
    for i, row in enumerate(resultat):
        if i % 2 == 0:
            table.insert('', 'end', values=row, tags=('evenrow',))
        else:
            table.insert('', 'end', values=row, tags=('oddrow',))

    maBase.close()

def afficherEnseignant():
    frame_etudiant =  tk.Frame(window)
    frame_etudiant.place(x=400, y=150, width=1120, height=500)

    table = ttk.Treeview(frame_etudiant, columns= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), height= 11, show = "headings")
    table.place(x = 0, y = 0, width = 1120, height=500)

    table.heading(1, text="ID")
    table.heading(2, text="Nom")
    table.heading(3, text="Prenom")
    table.heading(4, text="Email")
    table.heading(5, text="Tel")
    table.heading(6, text="Sexe")
    table.heading(7, text="Numero Urgence 1")
    table.heading(8, text="Numero Urgence 2")
    table.heading(9, text="Classe")
    table.heading(10, text="Date Naissance")
    table.heading(11, text="Lieu Naissance")

    table.column(1, width = 5)
    table.column(2, width = 50)
    table.column(3, width = 50)
    table.column(4, width = 80)
    table.column(5, width = 60)
    table.column(6, width = 10)
    table.column(7, width = 30)
    table.column(8, width = 50)
    table.column(9, width = 30)
    table.column(10, width = 50)
    table.column(11, width = 70)

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="inptic")
    meConnect = maBase.cursor()
    meConnect.execute("select * from users")
    resultat = meConnect.fetchall()
    # for row in resultat:
    #     table.insert('', 'end', value=row)
    table.tag_configure('evenrow', background='#d1faff')
    table.tag_configure('oddrow', background='#fff9d4')
    for i, row in enumerate(resultat):
        if i % 2 == 0:
            table.insert('', 'end', values=row, tags=('evenrow',))
        else:
            table.insert('', 'end', values=row, tags=('oddrow',))

    maBase.close()


# fonctions

# widgets
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=879,
    width=1522,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    368.0,
    0.0,
    1540.0,
    130.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    368.0,
    879.0,
    fill="#2A4163",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=afficherEtudiant,
    relief="flat"
)
button_1.place(
    x=0.0,
    y=190.0,
    width=368.0,
    height=85.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=afficherEnseignant,
    relief="flat"
)
button_2.place(
    x=0.0,
    y=275.0,
    width=368.0,
    height=85.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command="",
    relief="flat"
)
button_3.place(
    x=0.0,
    y=360.0,
    width=368.0,
    height=85.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command="",
    relief="flat"
)
button_4.place(
    x=0.0,
    y=445.0,
    width=368.0,
    height=85.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command="",
    relief="flat"
)
button_5.place(
    x=0.0,
    y=530.0,
    width=368.0,
    height=85.0
)
# widgets


# window.resizable(False, False)
window.mainloop()
