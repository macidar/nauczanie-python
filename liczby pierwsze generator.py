# poda określoną ilość liczb pierwszych
# potrzebny będzie moduł math i metoda math.sqrt(x)
# zamiast funkcji range będzie użyta pętla bo będzie dużo obliczeń a pętla jest szybsza
ilosc=int(input("Podaj ile chcesz liczb pierwszych: "))
import math

liczpetligl=1
liczba=1
liczbypier=[]
dzielnik=2
while liczpetligl<ilosc:
        # generacja liczb niparzystych do sprawdzenia
    liczba=liczba+2
    dzielnik=2
    while liczba%dzielnik!=0 and dzielnik<math.sqrt(liczba):
                    dzielnik=dzielnik+1
    if liczba%dzielnik!=0 :liczbypier.append(liczba)       
    liczpetligl=len(liczbypier)
print (liczbypier)