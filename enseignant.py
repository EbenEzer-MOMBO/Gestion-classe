from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

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
def MenuEtudiant():
    window.destroy()
    import etudiant
def MenuEnseignant():
    window.destroy()
    import enseignant
def MenuCours():
    window.destroy()
    import cours
def MenuClasse():
    window.destroy()
    import classes
def MenuAdmin():
    window.destroy()
    import admin
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
    command=MenuEtudiant,
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
    command=MenuEnseignant,
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
    command=MenuCours,
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
    command=MenuClasse,
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
    command=MenuAdmin,
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
