
# 🎲 Jeu de Boules – Projet Python / NSI

## Description
Ce projet est une **simulation d’un jeu de stratégie** en Python, développée dans le cadre du programme de **Terminale NSI**.  
Le principe est simple : deux joueurs retirent alternativement **1 ou 2 boules** d’une pile, et le **dernier à jouer gagne**.  

Le programme inclut un **mécanisme d’apprentissage** basé sur l’expérience : chaque case mémorise les coups qui ont mené à la victoire ou à la défaite et ajuste le nombre de boules disponibles pour chaque action, simulant ainsi un apprentissage simple.

---

## 🎮 Fonctionnalités

- ✅ **Simulation automatique** de parties entre deux joueurs IA  
- ✅ **Apprentissage basé sur les résultats** : les positions gagnantes sont renforcées, les positions perdantes pénalisées  
- ✅ **Répartition dynamique des boules** pour chaque case (jaune = action 1, rouge = action 2)  
- ✅ Affichage d’un **récapitulatif théorique et appris** pour chaque case  
- ✅ Mise en évidence des **positions gagnantes et perdantes**  

---

## ⚡ Installation

```bash
git clone https://github.com/AntoCheMaestro/ia_jeu_de_nim.git
cd ia_jeu_de_nim
python ia.py
