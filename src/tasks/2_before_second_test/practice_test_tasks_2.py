# # Teller hvor mange tresifrede palindromer det finnes
# antall = 0  # teller for antall palindromer

# # Gå gjennom alle tresifrede tall (100 til 999)
# for h in range(100, 1000):
#     t = h      # lagre originaltallet
#     s = 0      # tallet som skal bli baklengs

#     # Snur tallet
#     while h != 0:
#         r = h % 10       # ta siste siffer
#         s = s * 10 + r      # bygg baklengstallet
#         h = h // 10   # fjern siste siffer

#     # Sjekk om tallet er palindrom
#     if t == s:
#         print(t)            # viser selve palindromene
#         antall += 1         # øk teller

# # Vis resultatet
# print("Antall tresifrede palindromer:", antall)

print()

import json

befolkningsstatistikk: str = "data/Datasett_fodselstall.json"

with open(befolkningsstatistikk, encoding="utf-8") as befolkningsstatistikk:
    demografi_data: dict = json.load(befolkningsstatistikk)


datasett = demografi_data["dataset"]
dimensjon = datasett["dimension"]
tid = dimensjon["Tid"]
informasjon = datasett["value"]
år_labels = tid["category"]["label"]

print(f"{'År':^10} | {'Fødselstall':^15} | {'Innflyttinger':^17} | {'Utflyttinger':^18} | {'Netto Folkevekst':^20}")
print("---" * 33)

for i, år in enumerate(sorted(år_labels.keys(), key=int)):
    if informasjon[i*3] is not None:
        fødsel = informasjon[i*3]
    else:
        fødsel = 0
        
    if informasjon[i*3 + 1] is not None:
        innflytting = informasjon[i*3 + 1] 
    else:
        innflytting =  0
    
    if informasjon[i*3 + 2] is not None:
        utflytting = informasjon[i*3 + 2]
    else:
        utflytting = 0

    netto_folkevekst = fødsel + innflytting - utflytting
    
    print(f"{år:^10} | {fødsel:^15} | {innflytting:^17} | {utflytting:^18} | {netto_folkevekst:^18}")