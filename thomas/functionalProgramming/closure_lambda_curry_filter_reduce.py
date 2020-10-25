#!/usr/bin/pyhon

def decription() :
    print(
    """ funktionale Programmierung: - seiteneffektfrei, von keinem Zustand abhängig

    https://www.youtube.com/watch?v=YZIUPOGx_ts&t=510s

    Vorteile funktionaler vs. imperativer Programmierung

        stateless, einfacher zu verstehen und zu testen, egal welche Reihenfolge der Methoden,
            kann leichter parallelisert werden

    (Rekursion)
    ---- Funktion höherer Ordnung
    - Funktion die eine andere Funktion als Argument bekommt 
    und/oder
    - Funktion die eine Funktion als Rückgabe hat
    - Bsp. map (funktionale Äquivalent der for-Schleife), filter (wie map nur lambda ist Prädikat), reduce

    ---- Closure
    - annonyme Funktion + Snapshot des Geltungsbereiches in sich diese Funktion befunden hat
    Bsp.: def mal(x: int) -> Callable[[int], int]; multipliziere_liste(xs: list, k: int) -> list

    ---- Lambda
    - annonyme Funktionen

    ---- Currying (nach Haskall Curry benannt: Programmiersprache Haskall nach ihm benannt)
    - Funktion mit Anzahl von Argumenten bei der ein Argument festgehalten 
        und eine Funktion mit einer Stelligkeit weniger zurückgegeben wird

    ---- Filter (Liste + Funktion ist ein Prädikat)
    - statt map eine weitere Funktion höherer Ordnung: filter 
        (lambda muss jetzt aber eiun Prädikat sein, also eine Funktion die Wahr oder Falsch zurückgibt)

    ---- Reduce oder "fold left" (Liste + zweistellige Funktion + Startwert)
    - nimmt eine Liste + zweistellige Funktion + Startwert und reduziert damit die Liste auf ein Element

    ---- list comprehensions (Listen-Abstraktion)
    Spezialität in Python
    statt: list(map(lambda x: x * k, xs)) jetzt: [x * k for x in xs]
    oder
    statt: list(map(lambda x: x * k, xs)) jetzt: [x * k for x in xs]

    """)
decription()

from typing import Callable

# Funktion höherer Ordnung, weil sie eine Funktion zurückgibt
def mal(x: int) -> Callable[[int], int]:
    #Subfunktion Closure und Reduce
    def mal_x(y : int) -> int:
        return x * y
    return mal_x

def multipliziere_liste(xs: list, k: int) -> list:
    mal_k = mal(k)
    # map gibt nur Iterator zurück, deshalb list
    return list(map(mal_k, xs))

def multipliziere_liste_lambda(xs: list, k: int) -> list:
    # map gibt nur Iterator zurück, deshalb list
    return list(map(lambda x: x * k, xs))

# multipliziere_liste_lambda mit Nutzung von Python-Listen-Abstraktion
def multipliziere_liste_lambda_lc(xs: list, k: int) -> list:
    return [x * k for x in xs]

def filter_liste(xs: list, k: int) -> list:
    # map gibt nur Iterator zurück, deshalb list
    return list(filter(lambda x: x > k, xs))

# filter_liste mit Nutzung von Python-Listen-Abstraktion
def filter_liste_lc(xs: list, k: int) -> list:
    return [x for x in xs if x > k]

from functools import reduce
def summer(xs: list) -> int: 
    return reduce(lambda x1, x2 : x1 + x2, xs, 0)

mal_drei = mal(3)
print("mal_drei = Closure mal(3) : {0}".format(mal_drei))

print("mal_drei(5) = {0}".format(mal_drei(5)))

factor = 4
liste = [1,4,3,7]
res = multipliziere_liste(liste,4)

print("mit {0} multipliziere_liste {1} = {2}".format(factor, liste, res))

aLambda = lambda x: x+1

print("a lambda funktion: {0}".format(aLambda))

res = multipliziere_liste_lambda(liste,4)
print("mit {0} multipliziere_liste_lambda {1} = {2}".format(factor, liste, res))

res = filter_liste(liste,3)
print("filter_liste {0} mit Prädikat Elemente > 3 = {1}".format(liste, res))

print("Summe (reduce) {0}; lambda: x1+x2; start: 0 = {1}".format(liste,summer(liste)))

res = multipliziere_liste_lambda_lc(liste,4)
print("mit {0} multipliziere_liste_lambda_lc {1} = {2}".format(factor, liste, res))

res = filter_liste_lc(liste,3)
print("filter_liste_lc {0} mit Prädikat Elemente > 3 = {1}".format(liste, res))

# funktionale Audrücke mit einer Zeile

def anzahl_gerade(xs: list):
    return [x for x in xs if x % 2 == 0]
print("anzahl_gearde {0} = {1}".format(liste, anzahl_gerade(liste)))

# curry
def foo(x: int, y: int, z: int):
    return x +y +z

def foo(x: int) -> Callable[[int], int]:
    def addiere_x(y : int) -> int:
        return x + y
    return addiere_x

print(foo(foo(5)(3))(2))

#bar = curry(foo, 5)
# bar = curry(foo,5)
# bar(3,2) -> 10 (5+3+2)

# mein_filter
# mein_filter(lambda x: x>3, [1,2,3,4,5] ) -> [4,5]
def gt(xs: list) -> list:
    return [x for x in xs if x > 3]
print("gt 3: {0} = {1}".format(liste,gt(liste)))
