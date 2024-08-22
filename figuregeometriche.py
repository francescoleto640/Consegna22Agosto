import math
i = (input("Premi 1 per il perimetro del quadrato \nPremi 2 per la circoferenza del cerchio \nPremi 3 per l' area del rettangolo:\n "))
if i == "1":
    lato = float(input("Inserisci la lunghezza del lato: "))
    perimetro = lato * 4
    print(f"Perimetro: {perimetro}")

elif i == "2":
    raggio = float(input("Inserisci il raggio del cerchio: "))
    circo = 2* math.pi * raggio
    print(f"Circonferenza: {circo}")

elif i == "3":
    base = float(input("Inserisci base del rettangolo: "))
    altezza = float(input("Inserisci altezza del rettangolo: "))
    area = base * 2 + altezza * 2
    print(f"Area: {area}")

else: 
    print("Scelta non valida")
    

