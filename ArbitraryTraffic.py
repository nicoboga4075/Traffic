#### Arbitrary Traffic : définition arbitraire du temps des feux de circulation

# Importation de toutes les fonctions de Tkinter et du module EasyGUI

from tkinter import *

import easygui


# Fonction récursive de gestion des feux

def start():

    # Valeurs globales (temps défini pour chaque feu)

    global t_red
    global t_orange
    global t_green


    # Premier cas : LED orange allumée


    if can.itemcget(led_orange, 'fill') == 'orange':

      # Passage au feu rouge (la LED orange s'éteint et la LED rouge s'allume)

        can.itemconfigure(led_red, fill = 'red')
        can.itemconfigure(led_orange, fill = 'white')
        can.itemconfigure(led_green, fill = 'white')


        # Signal pour le passage des piétons

        can.bell() # Pour les malentendants

        easygui.msgbox("Vous avez "+str(t_red)+" s pour traverser", title="Piéton")


        # Le feu reste rouge pendant t_red*1000 ms

        root.after(t_red*1000,start)


    # Deuxième cas : LED rouge allumée


    elif can.itemcget(led_red, 'fill') == 'red':

        # Passage au feu vert (la LED rouge s'éteint et la LED verte s'allume)

        can.itemconfigure(led_red, fill = 'white')
        can.itemconfigure(led_orange, fill = 'white')
        can.itemconfigure(led_green, fill = 'green')

        # Le feu reste vert pendant t_green*1000 ms

        root.after(t_green*1000,start)



    # Troisième cas : LED verte allumée


    elif can.itemcget(led_green, 'fill') == 'green':

     # Passage au feu orange (la LED verte s'éteint et la LED orange s'allume)

        can.itemconfigure(led_red, fill = 'white')
        can.itemconfigure(led_orange, fill = 'orange')
        can.itemconfigure(led_green, fill = 'white')

        # Le feu reste orange pendant t_orange*1000 ms

        root.after(t_orange*1000,start)



# Rqs: La méthode after permet à start de s'appeler elle-même pendant le délai fourni. On force la dernière LED à être éteinte pour ne pas avoir deux LED allumées.



# Création de l'interface graphique avec Tkinter


root=Tk()

root.title("Feu tricolore ")

can = Canvas(root, bg='dark grey',height=640,width=480)

feux=can.create_rectangle(100,100,290,590,width=5,fill='black')

can.pack(side=LEFT)

Button(root,text='Quitter',command=root.destroy).pack(side=BOTTOM)


# Création des LED (elles sont toutes éteintes par défaut avec le statut white)


led_red=can.create_oval(125,125,250,250,width=5,fill='white')
led_orange=can.create_oval(125,280,250,400,width=5,fill='white')
led_green=can.create_oval(125,405,250,530,width=5,fill='white')


# Initialisation du feu au rouge

can.itemconfigure(led_red, fill = 'red')


# Saisie des constantes de temps de chaque feu

t_red = int(input("Feu rouge (s): "))
t_orange = int(input("Feu orange (s): "))
t_green = int(input ("Feu vert (s): "))


# Lancement de la boucle

start()


# Traitement des événements de la fonction start (boucle infinie sauf si on appuie sur le bouton Quitter de l'interface ou si on force l'arrêt du programme en quittant l'IDE par exemple)


root.mainloop()


