#### Modèle Traffic (coefficient de congestion)

# Importation de toutes les fonctions de Tkinter et du module time

import time
from time import sleep
from tkinter import *


# Fonctions


def red_light(a,can):
    for i in range(a):
        red=can.create_oval(320,70,420,170, fill="red")
        tk.update()
        time.sleep(1)


def red_black(a,can):

    for i in range(a):
        red=can.create_oval(320,70,420,170, fill="black")
        tk.update()
        time.sleep(0.05)



def green_light(a,can,coeff=1):
    for i in range(a):
        green=can.create_oval(320,330,420,430, fill="green")
        tk.update()
        time.sleep(coeff)


def green_black(a,can):
    for i in range(a):
        green=can.create_oval(320,330,420,430, fill="black")
        tk.update()
        time.sleep(0.05)


def light_blink(can):

    red=can.create_oval(320,70,420,170, fill="red")
    green=can.create_oval(320,330,420,430, fill="black")
    orange=can.create_oval(320,200,420,300, fill ="black")


def lancer():

    bouton_lancer.pack_forget()

    l_main.pack_forget()

    label0.pack_forget()

    t_green=int(s0.get())

    s0.pack_forget()

    n_f1=int(s1.get())

    n_f2=int(s2.get())

    s1.pack_forget()

    s2.pack_forget()

    affichage_compteur['text'] = n_f1

    affichage_compteur2['text'] = n_f2

    tk.update_idletasks()

    coefficient_congestion= max(n_f1,n_f2)/min(n_f1,n_f2)

    t_green_congest=t_green*coefficient_congestion

    nb_cars=int(t_green_congest/5) # On suppose qu'une voiture met 5 secondes pour franchir le feu quand elle se situe dans la zone de 5 m (4m sa longueur + 1 m du feu)


    if (nb_cars>=n_f1):

        red_black(1,can_widgt)

        while n_f1 !=0:

            green_light(5,can_widgt)

            n_f1-=1

            affichage_compteur['text'] = n_f1

            tk.update_idletasks()

            time.sleep(0.05)

        green_black(1,can_widgt)

        red_light(1,can_widgt)

        red_black(1,can_widgt2)

        while n_f2 !=0:

            green_light(5,can_widgt2)

            n_f2-=1

            affichage_compteur2['text'] = n_f2

            tk.update_idletasks()

            time.sleep(0.05)

        green_black(1,can_widgt2)

        red_light(1,can_widgt2)


    else:

        while(n_f1!=0) or (n_f2!=0):

            if (n_f1!=0):

                red_black(1,can_widgt)

                for i in range(nb_cars):

                    green_light(5,can_widgt)

                    n_f1-=1

                    if n_f1<0:
                        n_f1=0

                    affichage_compteur['text'] = n_f1

                    tk.update_idletasks()

                    time.sleep(0.05)

                green_black(1,can_widgt)

                red_light(1,can_widgt)


            if(n_f2!=0):


                red_black(1,can_widgt2)

                for i in range(nb_cars):

                    green_light(5,can_widgt2)

                    n_f2-=1

                    if n_f2<0:
                        n_f2=0

                    affichage_compteur2['text'] = n_f2


                    tk.update_idletasks()

                    time.sleep(0.05)

                green_black(1,can_widgt2)

                red_light(1,can_widgt2)


tk=Tk()


can_widgt=Canvas(tk, width=500, height=500)
can_widgt.create_rectangle(300,50,440,450, fill='grey', outline='black')
can_widgt.create_rectangle(365,450,375,800, fill='grey', outline='black')


l = LabelFrame(tk, text="Problème des feux", padx=20, pady=20)
l.pack(fill="both", expand="yes")

l_main=Label(l, text="Je vous invite à rentrer les valeurs qui suivent")
l_main.pack()

label0 = Label(l, text='Durée du feu vert sans traffic')
label0.pack()
s0 = Spinbox(l, from_=5, to=60) # Au moins 5 secondes
s0.pack()


label1 = Label(l, text='Nombre de véhicules au F1')
label1.pack()
affichage_compteur = Label(l, text='')
affichage_compteur.pack()
s1= Spinbox(l, from_=1, to=20) # On suppose que la détection se fait sur 100m, que la longueur moyenne d'une voiture est 4 m et qu'il y a 1 mètre de distance entre chaque voiture
s1.pack()


label2= Label(l, text='Nombre de véhicules au F2')
label2.pack()
affichage_compteur2 = Label(l, text='')
affichage_compteur2.pack()
s2 = Spinbox(l, from_=1, to=20)
s2.pack()


can_widgt.pack(side=LEFT)


can_widgt2=Canvas(tk, width=500, height=500)
can_widgt2.create_rectangle(300,50,440,450, fill='grey', outline='black')
can_widgt2.create_rectangle(365,450,375,800, fill='grey', outline='black')
can_widgt2.pack(side=RIGHT)



light_blink(can_widgt)
light_blink(can_widgt2)

bouton_lancer = Button(l, text = "Commencer", command = lambda: lancer())
bouton_lancer.pack()


tk.mainloop()

