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


def yellow_light(a):
    for i in range(a):
        amber=can_widgt.create_oval(320,200,420,300, fill="yellow")
        tk.update()
        time.sleep(1)


def yellow_black(a):
    for i in range(a):
        amber=can_widgt.create_oval(320,200,420,300, fill="black")
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
    red=can_widgt.create_oval(320,70,420,170, fill="black")
    green=can_widgt.create_oval(320,330,420,430, fill="black")
    amber=can_widgt.create_oval(320,200,420,300, fill ="black")



tk=Tk()
t_end = time.time() + 5 * 60 # On réalise l'expérience sur 5 min
vitesse_max=80 # La vitesse maximale autorisée est 80 km/h
can_widgt=Canvas(tk, width=750, height=1000)
can_widgt.pack()
can_widgt.create_rectangle(300,50,440,450, fill='grey', outline='black')
can_widgt.create_rectangle(365,450,375,800, fill='grey', outline='black')


light_blink()



# Le feu tricolore est maintenu par défaut au vert.

# En cas de dépassement de la vitesse limite autorisée, le feu bascule à l’orange, puis au rouge. Ce mode de fonctionnement sanctionne les comportements de vitesse excessive.



while time.time() < t_end:   # Tant que les 5 minutes ne sont pas écoulées

      green_light(1)

      vitesse=int(input("Vitesse du véhicule (km/h): ")) # On détecte la vitesse du véhicule

      if vitesse>vitesse_max: # Le véhicule est en excès de vitesse

          green_black(1)
          yellow_light(5)
          yellow_black(1)
          red_light(20)
          red_black(1)


tk.mainloop()