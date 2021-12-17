#!/usr/bin/env python
# -*- coding: utf-8 -*-


def est_bissextile(annee):
    # On suppose que annee > 0
    pass

def order(values: list = None) -> list:
    pass


def anagrams(words: list = None) -> bool:

   pass

def contains_doubles(items: list) -> bool:

    pass


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    pass


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    sentence_split = sentence.split()
    letter_list = []
    for word in sentence_split:
        for letter in word:
            letter_list.append(letter)

    dict_letters = {}
    for letter in letter_list:
        dict_letters[letter] = letter_list.count(letter)

    list_letters = sorted(dict_letters.items(), key=lambda x: x[1], reverse=True)


    real_dict = {}
    for tup in list_letters:
        if tup[1] > 5:
            real_dict[tup[0]] = tup[1]

    x = real_dict
    print(x)

    return x


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")



    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
