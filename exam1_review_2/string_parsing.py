event = "attacker:togepi,defender:pikachu,damage:500"

#HOW TO PARSE:
#IDENTIFY TOKENS SEPARATING DATA
#SPLIT THEM
#THEM CONTINUE SPLITTING RESULTING TOKENS UNTIL YOU GET WHAT YOU NEED

eventsplitresult = event.split(',')
print(eventsplitresult)
attacker = eventsplitresult[0].split(':')[1]
defender = eventsplitresult[1].split(':')[1]
damage = int(eventsplitresult[2].split(':')[1])
print(f"{attacker} TEACHES {defender} a LESSON for {damage}")