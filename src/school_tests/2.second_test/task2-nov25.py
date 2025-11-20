print()
import json

with open("json-til-prove-nov-25.json", encoding="utf-8") as fil:
    data = json.load(fil)


alle_avganger = []
for fly in data["flyselskap"]:
    navn = fly["navn"]
    for avgang in fly["avganger"]:
        alle_avganger.append({
            "tid": avgang["tid"],
            "navn": navn,
            "destinasjon": avgang["destinasjon"]
        })


alle_avganger.sort(key=lambda x: x["tid"])


print(f'{"Flyselskap":^20}|{"Destinasjon":^20}|{"Avgang":^20}|')
print("-" * 65)
for avgang in alle_avganger:
    print(f'{avgang["navn"]:^20}|{avgang["destinasjon"]:^20}|{avgang["tid"]:^20}|')
