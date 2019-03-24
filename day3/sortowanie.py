osoby = [{"nazwisko": "Nowak", "waga": 75, "ulubione_dania": ["schabowy, pomidorowa"]},
        {"nazwisko": "Kowalski", "waga": 93, "ulubione_dania": ["sushi, rosol"]},
        {"nazwisko": "Kos", "waga": 110, "ulubione_dania": ["mielone, rosol, pomidorowa"]},
        {"nazwisko": "Baran", "waga": 82, "ulubione_dania": ["schabowy, pomidorowa, marchewka"]},
        {"nazwisko": "Soltys", "waga": 91, "ulubione_dania": ["chleb, schabowy, makaron"]},
        {"nazwisko": "Angol", "waga": 76, "ulubione_dania": ["schabowy, pomidorowa, karkowka"]}
        ]

osoby.sort(key=lambda o: o["nazwisko"])
print [o["nazwisko"] for o in osoby]

print "\n"
osoby.sort(key= lambda o: o["waga"])
print [o["nazwisko"] for o in osoby]

# odwrotna kolejnosc
print "\n"
osoby.sort(key=lambda o: o["nazwisko"], reverse=True)
print [o["nazwisko"] for o in osoby]

print "\n"
osoby.sort(key= lambda o: o["waga"], reverse=True)
print [o["nazwisko"] for o in osoby]

print "teraz sorted \n"
print sorted(osoby, key= lambda o: o["nazwisko"])

print "\n teraz cmp \n"
# key to jest po czym sortujemy, a cmp jak to robimy
print sorted(osoby, cmp=lambda x, y: 1 if x > y else -1,
                    key=lambda o: o["waga"])
                    
