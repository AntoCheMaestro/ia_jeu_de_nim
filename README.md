# Jeu de Boules – Projet Python / NSI

## Description
Ce projet est une simulation d’un jeu de stratégie en Python, développée dans le cadre du programme de Terminale NSI.  
Le principe du jeu est le suivant : deux joueurs retirent alternativement une ou deux boules d’une pile, et le dernier joueur à retirer une boule gagne la partie.

Le programme intègre un mécanisme d’apprentissage simple : chaque case conserve une mémoire des coups qui ont conduit à la victoire ou à la défaite et ajuste le nombre de boules disponibles pour chaque action afin d’améliorer le comportement des joueurs IA.

---

## Fonctionnalités

- Simulation automatique de parties entre deux joueurs IA
- Apprentissage par renforcement : les positions gagnantes sont renforcées et les positions perdantes sont pénalisées
- Répartition dynamique des boules pour chaque case (jaune = action 1, rouge = action 2)
- Affichage d’un récapitulatif théorique et observé pour chaque case
- Identification des positions gagnantes et perdantes

---

## Installation et exécution

1. Cloner le dépôt :

```bash
git clone https://github.com/AntoCheMaestro/ia_jeu_de_nim.git
cd ia_jeu_de_nim
python ia.py
