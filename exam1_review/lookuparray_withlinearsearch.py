names = ["gloom", "stunfisk", "chikorita","mimejr", "togepi", "gengar"]
health = [100,100,100,100,100,100]

#LINEAR SEARCH FOR INDEX WHEN INDEX NOT AVAILABLE

attacker = "chikorita"
defender = "stunfisk"
damage = 5

defenderindex = -1#unknown
for i in len(names):
    if names[i] == defender:
        defenderindex = i
        break

#found the index
#reduce health
health[defenderindex] -= damage