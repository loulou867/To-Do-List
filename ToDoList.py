import tkinter as tk

def ajouter_tache():
    tache = entry.get() # récupération du texte de la zone de texte " entry "
    if tache:
        liste_box.insert(tk.END, tache)
        entry.delete(0, tk.END)
        sauvegarder_liste()

def supprimer_tache():
    selection = liste_box.curselection() # séléctionne la tache
    if selection: # Et la supprime ensuite
        liste_box.delete(selection)
        sauvegarder_liste()

def sauvegarder_liste():
    with open("liste_taches.txt", "w") as fichier: # sauvegarde les lignes de la To Do List dans un fichier texte
        taches = liste_box.get(0, tk.END)
        for tache in taches:
            fichier.write(tache + "\n")

def charger_liste():
    try:
        with open("liste_taches.txt", "r") as fichier: # Il lit le fichier "liste_taches.txt et importe le texte
            for ligne in fichier:
                liste_box.insert(tk.END, ligne.strip())
    except FileNotFoundError:
        pass

# Création de la fenêtre principale
root = tk.Tk() # création de la fenetre
root.title("To Do List") # Ajoute un titre

# Cadre pour la liste de tâches
frame_liste = tk.Frame(root)
frame_liste.pack(pady=5) # Coordonnées du cadre

# Liste de tâches
liste_box = tk.Listbox(frame_liste, height=15, width=50)
liste_box.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar pour la liste de tâches
scrollbar = tk.Scrollbar(frame_liste)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Associer la scrollbar à la liste de tâches
liste_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=liste_box.yview)

# Cadre pour l'ajout de tâche
frame_ajout = tk.Frame(root)
frame_ajout.pack(pady=5)

# Entrée pour ajouter une tâche
entry = tk.Entry(frame_ajout, width=50)
entry.pack(side=tk.LEFT)

# Bouton pour ajouter une tâche
ajouter_btn = tk.Button(frame_ajout, text="Ajouter", width=10, command=ajouter_tache)
ajouter_btn.pack(side=tk.LEFT, padx=5)

# Bouton pour supprimer une tâche
supprimer_btn = tk.Button(root, text="Supprimer", width=10, command=supprimer_tache)
supprimer_btn.pack(pady=5)

# Charger la liste de tâches existante
charger_liste()

# Exécution de la boucle principale
root.mainloop()
