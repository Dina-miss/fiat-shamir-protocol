#!/usr/bin/env python3

import operations
import getpass
import random

class Proof:
    def __init__(self, N):
        self.N = N
        self.i = random.getrandbits(16)
        self.S = operations.modulo(self.i, 2, N)


    def generateProofByHonestProver(self):
        # r megadása és u kiszámítása
        self.r = int(getpass.getpass("A bizonyító adjon meg egy tetszőleges r-et: "))
        self.u = operations.modulo(self.r, 2, self.N)

        # Egy bit küldése
        self.c =int(input("A verifikáló adjon meg egy tetszőleges bitet (0 vagy 1): "))
        # print("A verifikáló által megadott bit: {0}".format(self.c))

        # A bizonyító kiszámítja a v = r * (i^b) mod N-et
        self.v = operations.modulo(self.r * (self.i ** self.c), 1, self.N)

        # Bizonyíték 
        self.theProof()
        self.verificationOfProof()

        print()
        print("r: {0}, c: {1}, v: {2}".format(self.r, self.c, self.v))
        
        return self.resultOfVerification()
    

    def generateProofByAttacker(self):
        guess = int(getpass.getpass("Mire tippel a támadó, milyen bitet fog adni a verifikáló? "))
        if guess == 0:
            # r megadása és u kiszámítása
            self.r = int(getpass.getpass("A bizonyító adjon meg egy tetszőleges r-et: "))
            self.u = operations.modulo(self.r, 2, self.N)

            # Egy bit küldése
            self.c =int(input("A verifikáló adjon meg egy tetszőleges bitet (0 vagy 1): "))
            print("A verifikáló által megadott bit: {0}".format(self.c))

            # Ha a bizonyító eltalálta a bitet
            if guess == self.c:
                # A bizonyító kiszámítja a v = r * (i^b) mod N-et
                self.v = operations.modulo(self.r, 1, self.N)
                print("A támadó elküldte a v értéket a verifikálónak.")

                # Bizonyíték
                self.theProof()
                self.verificationOfProof()

                print()
                print("r: {0}, c: {1}, v: {2}, támadó tippje: {3}".format(self.r, self.c, self.v, guess))
                
                return self.resultOfVerification()
            else:
                return False
        else:
            self.r = int(getpass.getpass("A bizonyító adjon meg egy tetszőleges r-et: "))
            self.u = operations.modulo(((self.r ** 2) / self.S), 1, self.N)

            # Egy bit küldése
            self.c = int(input("A verifikáló adjon meg egy tetszőleges bitet (0 vagy 1): "))
            print("A verifikáló által megadott bit: {0}".format(self.c))

            # Ha a bizonyító eltalálta a bitet
            if guess == self.c:
                # A bizonyító kiszámítja a v-t
                self.v = operations.modulo(self.r, 1, self.N)
                print(self.v)
                print("A támadó elküldte a v értéket a verifikálónak.")

                # Bizonyíték
                self.theProof()
                self.verificationOfProof()

                print()
                print("r: {0}, c: {1}, v: {2}, támadó tippje: {3}".format(self.r, self.c, self.v, guess))
                
                return self.resultOfVerification()
            else:
                return False


    def theProof(self):
        self.proof = operations.modulo(self.v, 2, self.N)
        

    def verificationOfProof(self):
        self.verification = operations.modulo((self.u * pow(self.S, self.c)), 1, self.N)
    

    def resultOfVerification(self):
        if self.proof == self.verification:
            return True
        else:
            return False