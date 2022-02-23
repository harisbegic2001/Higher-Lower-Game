import random as r
message = """
Dobrodošli u igricu pogađanja popularnosti
Balkanskih klubova, cilj je da pogodite
koji klub je popularniji po broju pratilaca
na instagramu, Sretno!

P.S. brojevi će biti izraženi u hiljadam
"""
print(message)

baza = {
    "Željezničar": 57.7,
    "Sarajevo": 53.9,
    "Zrinjski": 9.7,
    "Borac Banja Luka": 13.7,
    "Dinamo Zagreb": 296,
    "Hajduk Split": 175,
    "Rijeka": 45.6,
    "Osijek": 40.3,
    "Crvena Zvezda": 504,
    "Partizan": 188,
    "Vojvodina": 16,
    "Proleter": 50.4,
    "Maribor": 50,
    "Olimpija Ljubljana": 17.7,
    "Budućnost Podgorica": 7.9,
    "Fk Velež": 21.4,
    "Vardar": 12.5
}
key_list = list(baza.keys())
val_list = list(baza.values())

brojac = 0
option_a = key_list[r.randint(0,len(key_list)-1)]
popularity_a = val_list[key_list.index(option_a)]
while True:
    

    
    
    
    option_b = key_list[r.randint(0,len(key_list)-1)]
    popularity_b = val_list[key_list.index(option_b)]

    if option_a == option_b:
        continue

    print("Koji je klub poznatiji?")
    print(f"Klub A: {option_a}")
    print(f"Klub B: {option_b}")

    odgovor_korisnika = input("Unesite 'A' ili 'B': ")

    if odgovor_korisnika == "A":
        if popularity_a > popularity_b:
            print("Tačan Odgovor!")
            brojac += 1
            print(f"Vaši trenutni bodovi: {brojac}")
            option_a = option_b
            popularity_a = popularity_b
            continue
        else:
            print("Netačan odgovor :(")
            print(f"Vaš score: {brojac}")
            break

    elif odgovor_korisnika == "B":
            if popularity_b > popularity_a:
                print("Tačan Odgovor!")
                brojac += 1
                print(f"Vaši trenutni bodovi: {brojac}")
                option_a = option_b
                popularity_a = popularity_b
                continue
        
            else:
                print("Netačan odgovor :(")
                print(f"Vaš score: {brojac}")
                break
    
    