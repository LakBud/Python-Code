print()
# Task 1)

# cars: list = [
#     {"car_logo": "BMW", "KM_status": 320932093, "Price": 250000 },
#     {"car_logo": "Mercedes", "KM_status": 2303, "Price": 120120 },
#     {"car_logo": "Kia", "KM_status": 320, "Price": 3293 },
#             ]

# cars[0]["model"] = "M5"

# for key in cars[0].keys():
#     print(f"{key:^20} | ", end="")
# print()

# print("-----------------------" * len(cars[0].keys()))


# for car in cars:
#     for value in car.values():
#         print(f"{value:^20} | ", end="")
#     print()

# def manipulereBokstav(bokstav, n):
#     alfabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
#     posisjon = alfabet.index(bokstav)
#     nyPosisjon = (posisjon + n) % 29
#     return alfabet[nyPosisjon]

# def behandleTekst(tekst, n):
#     nyTekst = ""
#     for bokstav in tekst:
#         if bokstav.isalpha():
#             nyBokstav = manipulereBokstav(bokstav, n)
#             nyTekst += nyBokstav
#         else:
#             nyTekst += bokstav
    
#     return nyTekst


# print(behandleTekst("Hei på deg", 3))

# studenter = {
#     "s101": {"navn": "Amina", "alder": 17, "poeng": [78, 90, 88], "status": {"aktiv": True, "gebyr": 0}},
#     "s203": {"navn": "Jonas", "alder": 18, "poeng": [55, 60, 58], "status": {"aktiv": False, "gebyr": 150}},
#     "s330": {"navn": "Evelyn", "alder": 17, "poeng": [92, 87, 95], "status": {"aktiv": True, "gebyr": 0}},
#     "s404": {"navn": "Leo",  "alder": 19, "poeng": [40, 45, 50], "status": {"aktiv": False, "gebyr": 300}}
# }


# student_id = str(input("Skriv inn en student_ID: "))

# try:
#     g = sum(studenter[student_id]["poeng"]) / len(studenter[student_id]["poeng"])
#     høyeste_karakter = max(studenter[student_id]["poeng"])
#     lavest_karakter = min(studenter[student_id]["poeng"])

    
# except Exception as e:
#     print("Ugyldig Student-ID")
#     print(f"Meldig fra systemet: {e}")
    
# else:
#     print()
#     print(f"Elev: {student_id}")
#     print(f"Gjennomsnittskarakter til Eleven: {round(g)}")
#     print(f"Høyeste karakteren av elevene: {høyeste_karakter}")
#     print(f"Lavest karakter av elevene: {lavest_karakter}")

temperaturer = [5, 8, 6, 4, 7, 3, 9]

for index, temperatur in enumerate(temperaturer, start=1):
    if temperatur >= 7:
        print(f"Day: {index}|{temperatur:^3}C")