#!/usr/bin/env python3

import math
import operations as operations
import proof as proof

def main():

    # A verifikáló meghatározza a körök számát, vagyis hogy hányszor kell lefuttatni a bizonyíték generálását és annak bizonyítását
    k = int(input("Hány körben kell bizonyítania magát a bizonyítónak? "))

    role = int(input("Írja be a bizonyító szándékát (0: becsületes, 1: támadó): "))
    if role < 0 and role > 1:
        role = int(input("Nem jó értéket adott meg! Próbálja meg újra. (0: becsületes, 1: támadó) "))
    print()

    # Megvan a publikus kulcs első része
    process = proof.Proof(operations.setPrime())

    # Relatív prím legyen N és S
    while math.gcd(process.N, process.S) != 1:
        process.N = operations.setPrime()
    # print(math.gcd(process.N, process.S))

    # A publikus adatok kiíratása
    print("Nyilvános kulcspár: ")
    print("N: {0}, S: {1}".format(process.N, process.S))
    print()

    # A bizonyítások lefutása
    for i in range(0, k):
        print("============== {0}. kör: ==============".format(i))
        if role == 0:
            result = process.generateProofByHonestProver()
        else:
            result = process.generateProofByAttacker()

        if result == True:
            print("A verifikáció sikerült!")
        else: 
            print("A verifikáció nem sikerült, a bizonyító nem az, akinek mondja magát!")
            exit()


if __name__ == "__main__":
    main()