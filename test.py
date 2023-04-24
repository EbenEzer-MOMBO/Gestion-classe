import tkinter as tk
#from PIL import Image, ImageTk
from subprocess import call
from tkinter import ttk
import mysql.connector

root = tk.Tk()
root.title("menu")
root.geometry("1400x770+2+2")
root.resizable(False, False)


def etudiant():
    root.destroy()
    call(["python", "frame_etudiant.py"])


frame_menu =  tk.Frame(root , bg='#267DFF')
frame_menu.place(x=0, y=0, width=300, height=770)

""""
image = Image.open("jiji.jpg")
image_1 = image.resize((200 , 100))
photo = ImageTk.PhotoImage(image_1)
"""
#frame etudiant
frame_etudiant =  tk.Frame(root)
frame_etudiant.place(x=350, y=70, width=1000, height=670)

table = ttk.Treeview(frame_etudiant, columns= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), height= 11, show = "headings")
table.place(x = 0, y = 90, width = 1000, height=700)

table.heading(1, text="id")
table.heading(2, text="nom")
table.heading(3, text="prenom")
table.heading(4, text="email")
table.heading(5, text="tel")
table.heading(6, text="sexe")
table.heading(7, text="numeroUrgence1")
table.heading(8, text="numeroUrgence2")
table.heading(9, text="classe")
table.heading(10, text="dateNaissance")
table.heading(11, text="lieuNaissance")
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



#FRAME MENU
button_etudiant = tk.Button(frame_menu,  text="Etudiant", font=('Arial-boldMT'), padx=10, relief='flat', borderwidth=0.5, command=etudiant)
button_etudiant.place(x=0, y=200, width=298, height=50)
button_enseignant = tk.Button(frame_menu,  text="Enseignant", font=('Arial-boldMT'), padx=10, relief='flat'  )
button_enseignant.place(x=0, y=251, width=298, height=50)
button_cours = tk.Button(frame_menu,  text="Cours", font=('Arial-boldMT'), padx=10, relief='flat'  )
button_cours.place(x=0, y=302, width=298, height=50)
button_classe = tk.Button(frame_menu,  text="Classe", font=('Arial-boldMT'), padx=10, relief='flat'  )
button_classe.place(x=0, y=353, width=298, height=50)
button_actualiser = tk.Button(frame_menu,  text="Actualiser", font=('Arial-boldMT'), padx=10, relief='flat'  )
button_actualiser.place(x=0, y=404, width=298, height=50)

root.mainloop()