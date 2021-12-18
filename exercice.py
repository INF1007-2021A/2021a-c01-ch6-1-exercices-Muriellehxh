#!/usr/bin/env python
# -*- coding: utf-8 -*-



def order(values: list = None) -> list:
    valeurs = input('Écrire 10 valeurs séparées par des virgules:')
    list_valeurs = list(valeurs.split(','))
    list_numbers = []
    list_letters = []
    for val in list_valeurs:

        if val.isdigit():
            list_numbers.append(val)
        else:
            list_letters.append(val)
    full_list = sorted(list_letters) + sorted(list_numbers)

    return full_list


def anagrams(words: list = None) -> bool:

   chaine1 = input('Entrer une chaine:')
   chaine2 = input('Entrer une deuxieme chaine:')
   return set(chaine1) == set(chaine2)

def contains_doubles(items: list) -> bool:

    return set(items) == items


def best_grades(student_grades: dict) -> dict: # revise
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    for index, name in enumerate(student_grades):
        student_grades[name] = sum(student_grades.get(name))/len(student_grades.get(name))
    best_student = max(student_grades, key=student_grades.get)  # CAREFUL: form of get():  dictionary.get( key ) = value
    # this gives the KEY of the max value

    # CAREFUL when trying to find key when knowing value, use a for loop!!!!

    new_dict = {}
    new_dict[best_student] = student_grades[best_student]


    return new_dict



def frequence(sentence: str) -> dict:   # revise
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

    sorted_dict = dict(sorted(dict_letters.items(), key= lambda letter : letter[1], reverse=True))
    # revise this line


    dict_values_above = {}
    for letter in sorted_dict:
        if sorted_dict[letter] > 5:
            dict_values_above[letter] = sorted_dict[letter]
            print(f"Le caractere {letter} revient {dict_letters[letter]} fois")

    return dict_values_above



def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données

    n = 0
    livre_recette = {}
    for n in range(0,3):
        name = input('Insérer le nom de votre recette: ')
        ingredient = input('Écrire une série dingredients séparé par une virgule: ')
        livre_recette[name] = list(ingredient.split(','))
    print(livre_recette)
    return livre_recette


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input('insérer le nom: ')
    if nom in ingredients:
        value = ingredients[nom]
        print(value)
    else:
        print('La recette nest pasd ans le dictionaire')


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    # print(order())

    print(f"On vérifie les anagrammes...")
    # print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    # print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

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

