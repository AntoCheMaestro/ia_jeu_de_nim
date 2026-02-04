from random import randint

NOMBRE_BOULES_INIT = 20
class Case:
    def __init__(self, nombre_case: int, boules_jaune: int, boules_rouge: int):
        self.nombre_case = nombre_case
        self.boules_jaune = boules_jaune
        self.boules_rouge = boules_rouge

    def __eq__(self, o):
        return self.nombre_case == o.nombre_case
    
    def __repr__(self):
        return f'Case numéro {self.nombre_case}. Boules Jaunes: {self.boules_jaune}. | Boules Rouges: {self.boules_rouge}.'
    
    def reset(self):
        # Réinitialise la case (sauf contraintes de l'état 1)
        if self.nombre_case == 1:
            self.boules_jaune = NOMBRE_BOULES_INIT
            self.boules_rouge = 0
        elif self.nombre_case == 0:
            self.boules_jaune = 0
            self.boules_rouge = 0
        else:
            self.boules_jaune = NOMBRE_BOULES_INIT
            self.boules_rouge = NOMBRE_BOULES_INIT

    def ajouter_boule(self, num_boule: int):
        assert num_boule in (1, 2)
        if num_boule == 1:
            self.boules_jaune += 1
        else:
            self.boules_rouge += 1

    def supprimer_boule(self, num_boule: int):
        """Punition : on enlève 1 boule si possible (sans passer en négatif)."""
        assert num_boule in (1, 2)
        if num_boule == 1:
            if self.boules_jaune > 0:
                self.boules_jaune -= 1
        else:
            if self.boules_rouge > 0:
                self.boules_rouge -= 1
                
    def recap(self):
        total = self.boules_jaune + self.boules_rouge
    
        print(f"\nCase {self.nombre_case}")
        print(f"  Boules jaunes (prendre 1) : {self.boules_jaune}")
        print(f"  Boules rouges (prendre 2) : {self.boules_rouge}")
    
        # --- Cas terminal ---
        if self.nombre_case == 0:
            print("  Position terminale : partie finie.")
            return
    
        # --- Théorie ---
        if self.nombre_case % 3 == 0:
            print("  Théorie : POSITION PERDANTE (multiple de 3)")
            print("  Aucun coup gagnant garanti.")
        else:
            coup_theorique = self.nombre_case % 3
            print("  Théorie : POSITION GAGNANTE")
            print(f"  Coup optimal théorique : prendre {coup_theorique}")
    
        # --- Apprentissage observé ---
        if total == 0:
            print("  ✅ IA : Comportement normal pour une position perdante")
            return
    
        if self.boules_jaune > self.boules_rouge:
            coup_ia = 1
        elif self.boules_rouge > self.boules_jaune:
            coup_ia = 2
        else:
            coup_ia = None
    
        if coup_ia is None:
            print("  IA : indécise (répartition équilibrée)")
        else:
            print(f"  IA : préfère prendre {coup_ia}")
    
        # --- Comparaison ---
        if self.nombre_case % 3 != 0 and coup_ia == self.nombre_case % 3:
            print("  ✅ Apprentissage COHÉRENT avec la théorie")
        elif self.nombre_case % 3 == 0:
            print("  ✅ Comportement normal pour une position perdante")
        else:
            print("  ❌ Apprentissage NON cohérent (bruit ou reset)")


class Joueur:
    def __init__(self, num_j):
        self.num_j = num_j
        
    def __repr__(self):
        return 'Joueur '+str(self.num_j)

    def tire_une_boule(self, case: Case):
        total = case.boules_jaune + case.boules_rouge
        if total == 0:
            case.reset()
            total = case.boules_jaune + case.boules_rouge


        tirage = randint(1, total)
        if tirage <= case.boules_jaune:
            return 1  # jaune => prendre 1
        else:
            return 2  # rouge => prendre 2


# --- Initialisation des cases ---
c0 = Case(0, 0, 0)
c1 = Case(1, NOMBRE_BOULES_INIT, 0)  # à 1 bâton restant, seule action possible = prendre 1 (jaune)
c2 = Case(2, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)
c3 = Case(3, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)
c4 = Case(4, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)
c5 = Case(5, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)
c6 = Case(6, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)
c7 = Case(7, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)
c8 = Case(8, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)
c9 = Case(9, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)
c10 = Case(10, NOMBRE_BOULES_INIT, NOMBRE_BOULES_INIT)

liste_cases = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

joueur1 = Joueur(1)
joueur2 = Joueur(2)


def tour(j1: Joueur, j2: Joueur):

    liste_jeu_j1 = []  # liste de (etat, action)
    liste_jeu_j2 = []

    case_actuelle = 10
    joueur1_joue = True
    dernier_joueur = None  # 1 ou 2

    while case_actuelle != 0:
        case_obj = liste_cases[case_actuelle]

        if joueur1_joue:
            action = j1.tire_une_boule(case_obj)  # 1 ou 2
            liste_jeu_j1.append((case_actuelle, action))
            case_actuelle -= action
            dernier_joueur = 1
        else:
            action = j2.tire_une_boule(case_obj)
            liste_jeu_j2.append((case_actuelle, action))
            case_actuelle -= action
            dernier_joueur = 2

        joueur1_joue = not joueur1_joue


    gagnant = j1 if dernier_joueur == 1 else j2
    perdant = j2 if dernier_joueur == 1 else j1


    # Apprentissage :
    # - gagnant : on ajoute 1 boule pour chaque action jouée
    # - perdant : on enlève 1 boule pour chaque action jouée
    if perdant is j1:
        # j1 perd, j2 gagne
        for (etat, action) in liste_jeu_j1:
            liste_cases[etat].supprimer_boule(action)
        for (etat, action) in liste_jeu_j2:
            liste_cases[etat].ajouter_boule(action)
    else:
        # j2 perd, j1 gagne
        for (etat, action) in liste_jeu_j2:
            liste_cases[etat].supprimer_boule(action)
        for (etat, action) in liste_jeu_j1:
            liste_cases[etat].ajouter_boule(action)

    return gagnant


for _ in range(1000): #100020 Pour resultat hyper coherent
    tour(joueur1, joueur2)
for case in liste_cases[1:]:
    case.recap()