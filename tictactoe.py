import tkinter as tk

# Initialisation de la fenêtre
fenetre = tk.Tk()
fenetre.title("Tic Tac Toe")

# Création des variables
joueur_actuel = 'X'
cases = {}
gagne = False

# Fonction qui vérifie si un joueur a gagné
def verifier_gagne():
    global gagne
    # Vérification des alignements horizontaux
    for i in range(3):
        if cases[i,0]['text'] == cases[i,1]['text'] == cases[i,2]['text'] != '':
            cases[i,0].config(bg='green')
            cases[i,1].config(bg='green')
            cases[i,2].config(bg='green')
            gagne = True
    # Vérification des alignements verticaux
    for j in range(3):
        if cases[0,j]['text'] == cases[1,j]['text'] == cases[2,j]['text'] != '':
            cases[0,j].config(bg='green')
            cases[1,j].config(bg='green')
            cases[2,j].config(bg='green')
            gagne = True
    # Vérification des alignements diagonaux
    if cases[0,0]['text'] == cases[1,1]['text'] == cases[2,2]['text'] != '':
        cases[0,0].config(bg='green')
        cases[1,1].config(bg='green')
        cases[2,2].config(bg='green')
        gagne = True
    if cases[0,2]['text'] == cases[1,1]['text'] == cases[2,0]['text'] != '':
        cases[0,2].config(bg='green')
        cases[1,1].config(bg='green')
        cases[2,0].config(bg='green')
        gagne = True

# Fonction qui gère le clic sur une case
def clic_case(row, column):
    global joueur_actuel
    global gagne
    if cases[row,column]['text'] == '' and not gagne:
        cases[row,column]['text'] = joueur_actuel
        if joueur_actuel == 'X':
            joueur_actuel = 'O'
        else:
            joueur_actuel = 'X'
        verifier_gagne()
        if not gagne:
            match_nul = True
            for i in range(3):
                for j in range(3):
                    if cases[i,j]['text'] == '':
                        match_nul = False
            if match_nul:
                for i in range(3):
                    for j in range(3):
                        cases[i,j].config(bg='red')
                gagne = True

# Création des cases
for i in range(3):
    for j in range(3):
        cases[i,j] = tk.Button(fenetre, text='', font=('Helvetica', 40), width=2, height=1, command=lambda row=i, column=j: clic_case(row, column))
        cases[i,j].grid(row=i, column=j)

# Lancement de la boucle principale
fenetre.mainloop()