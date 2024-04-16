[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/E_L8YDkF)
# Domácí úkol č. 10
> **Upravujte pouze soubor `assignment_10_1.py`!**

## Counting Sort
Cílem tohoto cvičení (kromě drobného opakování) je implementace algoritmu *Counting Sort* pro abecední řazení načteného
textu. Při implementaci postupujte dle návodu níže.


### Balíček `os` 
* Do modulu `assignment_10_1.py` importujte balíček `os`.
* V dokumentaci zjistěte, pomocí jaké metody z balíčku `os.path` můžete zjistit, zda-li v pracovním adresáři existuje
soubor s požadovaným názvem.

### Načtení dat
* Do modulu `assignment_10_1.py` implementujte funkci `read_data()`.
* Funkce bude mít dva vstupní parametry:
  * První parametr bude reprezentovat název souboru se zdrojovými daty, např.: `famous_quotes.txt`.
  * Druhý parametr bude reprezentovat index řádku, ze kterého v textovém souboru budete načítat řetězec.
* Funkce pomocí vhodné metody z balíčku `os.path` zjistí, jestli v pracovním adresáři existuje soubor, který chce
  načíst. Pokud ne, vrátí hodnotu `None`. Stejně tak vrátí `None` i pro řádek, který v souboru neexistuje.
* Funkce načte větu z požadovaného řádku textového souboru.
* Funkce vrátí načtenou větu jako seznam jednotlivých slov převedených na malé znaky. Seznam nebude obsahovat
  interpunkční znaménka obsažená na **konci věty**.

### Tokenizace slov
Algoritmus *Counting Sort* umí řadit pouze celá čísla. Úkolem je ovšem abecední řazení slov. Jednoduchý způsob,
jak toto omezení obejít, je přiřadit každému slovu nějaký identifikátor (token), v tomto případě celé číslo. 
Protože by řazení mělo být prováděno abecedně dle prvního znaku slova, je možné toto celé číslo odvodit právě z
prvního znaku (slova začínající stejným znakem tak budou mít stejný token).

* Do modulu `assignment_10_1.py` implementujte funkci `tokenize()`.
* Funkce bude mít jeden vstupní parametr reprezentující neseřazený seznam slov.
* Funkce vrátí seznam celých čísel, který odpovídá prvním znakům každého slova (pořadí musí být zachováno).
  Pro převod na pořadí znaku abecedy využijte funkci `ord`.
* Vzorová vstupní a výstupní data mohou vypadat např. takto:

Vstup: `["ave", "caesar"]`; Výstup: `[97, 99]`

### Seřazení a zjištění četnosti slov
* Do souboru `assignment_10_1.py` implementujte funkci `counting_sort()`.
* Funkce bude mít jeden vstupní parametr, který bude reprezentovat seznam slov získaný v bodu *Načtení dat*.
* Funkce zavolá funkci `tokenize()`, převede seznam slov na seznam tokenů (celých čísel).
* Funkce pomocí metody *Counting Sort* zajistí **vzestupné** abecední seřazení slov načtené věty. 
* Funkce bude mít jeden výstup a to **slovník** obsahující klíče `"sorted_sequence"` a `"frequency"`. Pod klíčem 
  `"sorted_sequence"` bude uložen seznam seřazených slov. Pod klíčem `"frequency"` bude uložen seznam o délce 256 prvků
  obsahující **kumulativní četnosti** slov se stejným počátečním znakem. Tento seznam je mezikrokem metody
  *Counting Sort*. Doporučujeme použít metodu `.copy()`, abyste při následných operacích nepřišli o původní kumulativní
  četnost, která má být použita na výstupu funkce.

### Docstring
* Ke každé funkci doplňte stručný dokumentační řetězec.

## Trochu teorie k algoritmu:

### Counting Sort - obecné vysvětlení
*Counting Sort* je třídicí algoritmus, který třídí prvky seznamu počítáním počtu výskytů každého jedinečného prvku 
v seznamu. Počet je uložen v pomocném seznamu a třídění se provádí mapováním počtu jako indexu pomocného seznamu.

#### Krok č. 1
Inicializace seznamu pro určení četností jednotlivých prvků. Protože pracujete se znaky abecedy a všechny základní znaky
se v Pythonu vyskytují v rozsahu 0–255, vytvořte seznam obsahující 256 nulových hodnot. Tento seznam bude využit pro 
ukládání počtu prvků v seznamu.

![1](https://cdn.programiz.com/cdn/farfuture/bRDNfPQG8lie6m7EFXVqPj8w6RzkRhM34XNaAoG2dCs/mtime:1582112622/sites/tutorial2program/files/Counting-sort-1.png)

#### Krok č. 2
Inicializace seznamu pro ukládání seřazených slov. Vytvořte seznam s takovým počtem prvků, kolik má vstupní neseřazená
sekvence. Výchozí hodnota prvků může být libovolná, např. `0` nebo `""`.

![1](https://cdn.programiz.com/cdn/farfuture/bRDNfPQG8lie6m7EFXVqPj8w6RzkRhM34XNaAoG2dCs/mtime:1582112622/sites/tutorial2program/files/Counting-sort-1.png)

#### Krok č. 3
Sekvenčně projděte seznam s tokeny (analyzujete totiž celá čísla reprezentující text).
Do seznamu s četnostmi uložte četnost každého tokenu. Četnost tokenu ukládáte na pozici odpovídající hodnotě tokenu.
Pokud máte např. 5 tokenů s hodnotou `123`, uložíte do seznamu s četnostmi na pozici `123` hodnotu 5. Pokud token 
neexistuje, zůstane v seznamu četností na jeho pozici hodnota `0`.
![2](https://cdn.programiz.com/cdn/farfuture/CIyC1Lkj5JFln_hjy8U1acmUZ4JST__v4bQBvPcnOkk/mtime:1582112622/sites/tutorial2program/files/Counting-sort-2.png)

#### Krok č. 4
Projděte seznam s četnostmi a převeďte je na kumulativní četnosti (kumulativní četnost na pozici `i` bude dána
součtem všech četností v rozsahu `0:i`, včetně). Jednoduchá implementace může spočívat např. v sekvenčním průchodu
seznamem a s pomocí indexace provést v každé iteraci kumulaci dvou po sobě jdoucích hodnot:

`count[i] += count[i - 1]`

Tento výsledek je použit při umisťování prvků do správného indexu seřazeného seznamu. Obrázek níže odpovídá správně
určeným kumulativním četnostem pro seznam z Kroku č. 3.
![3](https://cdn.programiz.com/cdn/farfuture/6A5S6vY-KsapHcyBjGgLNrp-58NRdyGDeVXspSzUbwM/mtime:1582112622/sites/tutorial2program/files/Counting-sort-3.png)

#### Krok č. 5
A teď nás čeká kouzlo celého algoritmu :) Označte si kumulativní četnost konkrétního prvku jako `cf`. Potom hodnota 
`cf - 1` označuje pořadí tohoto prvku v seřazené sekvenci!
V příkladu níže je na první pozici token s hodnotou `4`. Jeho kumulativní četnost tedy naleznete v seznamu kumulativních
četností na indexu `4` (5. prvek). Na této pozici leží hodnota `6`. Po odečtení jedničky tedy získáte index toho prvku
v seřazené sekvenci. První prvek z původní sekvence bude v seřazené sekvenci vložen na index číslo `5`. V tomto případě
může být postup následující:

* Sekvenčně projděte seznam s tokeny (nejlépe pomocí indexace nebo po "zipnutí" se seznamem slov).
* Pro každý token najděte jeho kumulativní četnost a od této hodnoty odečtěte jedničku.
* Do seznamu pro ukládání seřazených slov uložte na index z bodu 2 slovo z neseřazeného seznamu, jehož pořadí odpovídá
  pořadí právě analyzovaného tokenu.
* Po umístění prvku do správné polohy snižte jeho kumulativní četnost o jeden (aby nebyly nepřiřazovány stejné tokeny 
  vždy do jedné pozice).
* A je seřazeno!

> Counting Sort je **stabilní** třídí algoritmus. Pozor tedy na zachování relativního pořadí jednotlivých slov. 
> Kumulativní četnost určuje vždy poslední výskyt stejného prvku. Pokud však řadíte slova od prvního po poslední, 
> bude důsledkem změna směru relativního pořadí (stejné prvky budou seřazeny v opačném pořadí oproti původní sekvenci). 
> Problém můžete vyřešit buď **reverzním procházením** řazené sekvence nebo vhodnou úpravou indexace při plnění seřazené
> sekvence.

![4](https://cdn.programiz.com/cdn/farfuture/tcfjQdeYwL_jETOCPZxNjIXbysRrb7MaG6PwO2MzHnM/mtime:1582112622/sites/tutorial2program/files/Counting-sort-4_1.png)



    


