#dzielniki
# liczba=20
liczba=int(input("Podaj liczbę której dzielniki chcesz znaleźć "))
potdziel=[]
dzielniki=[]
i=2
while i<liczba:
    potdziel.append(i)
    i=i+1
for dziel in potdziel:
    if liczba%dziel==0:
        dzielniki.append(dziel)
print("liczba ",liczba," jest podzielna przez: ", dzielniki)
naj=dzielniki[-1]
print("Najwyższy dzielnik ",liczba, " to: ",naj)
