#### Red Traffic

# Le feu tricolore est maintenu par défaut au rouge.En cas d’approche d’un usager, le feu reste au rouge si l’automobiliste dépasse la vitesse autorisée, et le feu passe au vert si le véhicule est détecté en dessous de la vitesse limite autorisée.

# Importation de toutes les fonctions de Tkinter et du module time

import time
from time import sleep
from tkinter import *


# Fonctions


def red_light(a):
    for i in range(a):
        red=can_widgt.create_oval(320,70,420,170, fill="red")
        tk.update()
        time.sleep(1)


def red_black(a):
    for i in range(a):
        red=can_widgt.create_oval(320,70,420,170, fill="black")
        tk.update()
        time.sleep(0.5)


def orange_light(a):
    for i in range(a):
        orange=can_widgt.create_oval(320,200,420,300, fill="orange")
        tk.update()
        time.sleep(1)


def orange_black(a):
    for i in range(a):
        orange=can_widgt.create_oval(320,200,420,300, fill="black")
        tk.update()
        time.sleep(0.5)


def green_light(a):
    for i in range(a):
        green=can_widgt.create_oval(320,330,420,430, fill="green")
        tk.update()
        time.sleep(1)


def green_black(a):
    for i in range(a):
        green=can_widgt.create_oval(320,330,420,430, fill="black")
        tk.update()
        time.sleep(0.5)


def light_blink():

    red=can_widgt.create_oval(320,70,420,170, fill="red")
    green=can_widgt.create_oval(320,330,420,430, fill="black")
    orange=can_widgt.create_oval(320,200,420,300, fill ="black")


vitesse=0

def v_vehicle():

    btn2['state'] = DISABLED

    global vitesse

    vitesse=int(input("Vitesse du véhicule (km/h): ")) # On détecte la vitesse du véhicule

    red_black(1)

    if vitesse <= vitesse_max: # Le véhicule respecte la vitesse autorisée

        green_light(35)
        green_black(1)
        orange_light(5)
        orange_black(1)

    else :

        pass

    red_light(1)

    btn2['state'] = NORMAL


tk=Tk()
t_end = time.time() + 5 * 60 # On réalise l'expérience sur 5 min
vitesse_max=80 # La vitesse maximale autorisée est 80 km/h
can_widgt=Canvas(tk, width=750, height=500)

can_widgt.create_rectangle(300,50,440,450, fill='grey', outline='black')
can_widgt.create_rectangle(365,450,375,800, fill='grey', outline='black')

can_widgt.pack(side=LEFT)


btn1=Button(tk,text='Quitter',command=tk.destroy).pack(side=BOTTOM)

btn2=Button(tk,text='Véhicule',command=v_vehicle)
btn2.pack(side=BOTTOM)

light_blink()



tk.mainloop()