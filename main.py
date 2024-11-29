"""
renvoie le nombre d'occurence à l'aide des tuples
"""
# on augmente le nombre de récursivités autorisés afin de passer les tests
import sys
sys.setrecursionlimit(1035)

#### Fonctions secondaires

def artcode_i(s):
    """Encode une chaîne de caractères en une liste de tuples 
    (caractère, nombre d'occurrences) selon un algorithme itératif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: Une liste de tuples (caractère, nombre d'occurrences).
    """
    resultat = [(s[0], 1)]
    k = 1
    n = len(s)
    while k < n:
        if s[k] == resultat[-1][0]:
            resultat[-1] = (resultat[-1][0], resultat[-1][1] + 1)
        else:
            resultat.append((s[k], 1))
        k += 1
    return resultat


def artcode_r(s):
    """Retourne la liste de tuples encodant une chaîne
    de caractères passée en argument selon un algorithme récursif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: Une liste de tuples (caractère, nombre d'occurrences).
    """

    if not s:
        return []
    current_char = s[0]
    count = 1
    while count < len(s) and s[count] == current_char:
        count += 1

    return [(current_char, count)] + artcode_r(s[count:])


#### Fonction principale


def main():
    """
    Fonction main afin de tester avec différentes valeurs la compilation du code.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
