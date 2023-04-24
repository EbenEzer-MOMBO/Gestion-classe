from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from subprocess import call
import mysql.connector
import tkinter as tk


# configurations
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()
window.title("INPTIC - Gestionnaire études")
window.geometry("1540x879")
window.configure(bg="#FFFFFF")
# configurations

# fonctions

# widgets
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
    for row in resultat:
        table.insert('', 'end', value=row)

    maBase.close()
# widgets


# window.resizable(False, False)
window.mainloop()