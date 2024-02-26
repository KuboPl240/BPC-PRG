from random import randrange
cycles = int(input("Zadajte počet terčov: "))
for cycle in range(0,cycles):
    hits = 0
    for i in range(0,8):
        if randrange(0, 101)>45:
            hits = hits+1
    print(f"Terč číslo: {cycle+1} {hits/8*100}% úspešnosť")

