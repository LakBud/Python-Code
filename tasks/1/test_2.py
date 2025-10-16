# 1
print()
x = 1.5
y = "H&M"
print(f"Jeg liker {y} men jeg har bare {x} kr")

# 2
print()
b = "Jeg kjøpte Dogecoin også gikk den ned hard, big F"
print(b[44:49])

# 3
print()
c = "Språket mitt er HTML/PHP/Python"
print(f"{c}")


# 4
print()
g = 5.4309309309
t = 4.354905590

print(f"sum = {(g * t):^.3f}")

# 5
print()
kostyme_input = str(input("Har du en kostyme, svar enten ja eller nei: "))

if kostyme_input == "ja":
    print("Du kan komme inn bygget")
elif kostyme_input == "nei":
   print("Du kan ikke komme inn bygget")
else: 
  print("Du må svare enten ja eller nei")
    
    
# 6
låter_liste = ["F.R.I.E.N.D.S", "All Alone", "Bad", "Believer", "Fight Back", "Dior", "TFW"]
print()
print(låter_liste)
# 7
print()
print(låter_liste[3])

# 8 og 9
print()
låter_liste.remove("TFW")
låter_liste.insert(1, "Pride is the Devil")

print(låter_liste)