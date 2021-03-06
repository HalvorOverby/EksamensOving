import os #må endres for mac
from random import randint

def kapitler():
    kapitteler = {0: 'Alle', 1: 'Logic and Proofs', 2: 'Sets, Functions, Sequences, Sums and Matrices', 3: 'Algorithms',
                4: 'Number Theory and Cryptography', 5: 'Induction and Recursion', 6: 'Counting',
                8: 'Advanced Counting Techniques', 9: 'Relations', 10: 'Graphs', 11: 'Trees',
                13: 'Modeling Computation'}

    for key, val in kapitteler.items():
        print(key, val)
    print()

def spor(svar):
    global kapittel,shuffle, antalloppgavergjort, antalloppgaverklart
    svar=svar.lower()
    kap="0123456789101113alle"
    if svar in kap:
        if svar=="alle":
            svar=0
        svar=int(svar)
        if svar==7 or svar==12:
            spor(input("Dette kapittelet er ikke pensum, velg et annet\n"))
        else:
            if svar==0:
                kapittel=svar
                shuffle=1
            else:
                kapittel=svar
                shuffle=0
            oppgave(kapittel)
    elif svar=="feil" or svar=="i do not understand this question":
        oppgave(kapittel)
        antalloppgavergjort+=1
    elif svar=="neste":
        oppgave(kapittel)
    elif svar=="gjort":
        gjort(kapittel,current)
        oppgave(kapittel)
        antalloppgavergjort+=1
        antalloppgaverklart+=1
    elif svar=="lf":
        show(kapittel,-current)
    elif svar=="stats":
        prosent=int(antalloppgaverklart/antalloppgavergjort*100)
        print(prosent,"%")
        print("Dette tilsvarer en",karakter(prosent)) 
    
    else:
        os.startfile("Oppgaver\hmm.png") #må endres for mac
        spor(input("Forstod ikke komandoen. Skriv noe annet\n"))

def numberofexercises(kap):
    for i in range(1,50):
        try:
            open(f"Oppgaver\kap{kap}opg{i}.PNG")
        except IOError:
            return i-1
        
def karakter(prosent):
    if prosent in range(89,101): return "A"
    if prosent in range(77,89): return "B"
    if prosent in range(65,77): return "C"
    if prosent in range(53,65): return "D"
    if prosent in range(41,53): return "E"
    else: return "F"
    
def oppgave(kap):
    global current, recursion,kapittel,shuffle
    if kap==0 or shuffle==1:
        kap=randint(1,11)
        if kap==7:
            kap=13
            shuffle=1
        else:
            kapittel=kap
            shuffle=1
    antall=numberofexercises(kap)
    if antall<=1:
        exercise=1
    else:
        exercise = randint(1, antall)

    if recursion==500:
        spor(input("Med mindre du har gjort 500 oppgaver kan det ser ut som du er ferdig med dette kapittelet. Vendligst velg et nytt"))
        recursion = 0
    #du bør legge inn en funksjon som sjekker om man er feridig med alle oppgavene i et kapittel
    if not done(kap,exercise):
        current=exercise
        show(kap,exercise)
    else:
        recursion += 1
        oppgave(kap)


def show(kap,opg):
    os.startfile(f"Oppgaver\kap{kap}opg{opg}.PNG") #må endres for mac

def gjort(kap,opg):
    with open("Oppgaver\gjort.txt","a") as f:
        f.write(f"{kap},{opg} ")

def done(kap,opg):
    hele=""
    with open(f"Oppgaver\gjort.txt","r") as f:
        hele=f.read()
        hele=hele.split()
        if f"{kap},{opg}" in hele:
            return 1
        else:
            return 0

def main():
    kapitler()
    spor(input("Hvilket kapittel vil du jobbe med?(0-13)\n"))
    spor(input("\nDu kan skrive:\n'lf'    for løsningsforslag\n'neste' for å hoppe over og få en ny oppgave\n'gjort' for å markere en oppgave som gjort og få en ny\n'feil' hvis du har fått feil svar\nEt tall for et nytt kapittel\n'Stats' for antall prosent riktige\n"))
    while True:
        spor(input("\nMuligheter:\n-'lf'\n-'neste'\n-'gjort'\n-'feil'\n-Nummeret til et kapittel\n-'Alle' for shuffle\n-'Stats' for antall riktige\n"))
recursion=0
kapittel=0
current=0
shuffle=0
antalloppgavergjort=0
antalloppgaverklart=0
main()

