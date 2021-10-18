#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        pass


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        while len(words) < 2:
            words.append(input('svp entrez un mot\n'))

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    return len(set(items)) != len(items)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.values():
        average = sum(value) / len(value)

        if len(best_student) == 0 or list(best_student.values())[0] < average:
            best_student = {key: average}

    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    frequency = dict()
    for letter in sentence:
        frequency[letter]

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Quel est le nom de votre recette?\n")
    ingredients = input("Entrez la liste d'ing ? Séparer ingrédients par une virgule\n").split(",")

    return {name: ingredients}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Quel est le nom de la recette?\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("Je ne connais pas!!")
        print_recipe(ingredients)


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
