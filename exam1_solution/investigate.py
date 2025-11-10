#GET COLLECTOR NAME
spotifyfile = open("SPOTIFY_PRIVATE_PLAYLIST_BEST_OF_BEETLES_SONGS.txt","r")
collectorname = spotifyfile.readline().strip()
spotifyfile.close()

#LOAD ALL MEMBER NAMES IN A LIST INDEXED BY ID
names = [""]*100
for i in range(100):
    memberfile = open(f"members/member_ID{i}.txt", "r")
    names[i] = memberfile.readline().strip()
    memberfile.close()

#FIND COLLECTOR INDEX BY NAME
collectorid = -1
for i in range(100):
    if names[i] == collectorname:
        collectorid = i
        break

#LOAD TRANSACTIONS IN A LIST
transactionsfile = open("transactions.txt", "r")
transactionlines = transactionsfile.readlines()
transactionsfile.close()

#PARSE TRANSACTIONS INTO 3 PARALLEL LISTS
fromlist = []
tolist = []
amountlist = []
for line in transactionlines:
    line = line.strip()
    parts = line.split("|")
    fromid = int(parts[0].split(":")[1])
    toid = int(parts[1].split(":")[1])
    amount = int(parts[2].split(":")[1])
    fromlist.append(fromid)
    tolist.append(toid)
    amountlist.append(amount)

numberoftransactions = len(transactionlines)

#CALCULATE TOTAL AMOUNT OF MONEY EVERY MEMBER RECEIVED FROM THE COLLECTOR
total_amount_received_from_the_collector = [0]*100

for i in range(numberoftransactions):
    if fromlist[i] == collectorid:
        total_amount_received_from_the_collector[tolist[i]] += amountlist[i]

#BOSS RECEIVED THE MOST AMOUNT OF MONEY FROM THE COLLECTOR
bossid=-1
maxreceived=0
for i in range(100):
    if total_amount_received_from_the_collector[i] > maxreceived:
        maxreceived = total_amount_received_from_the_collector[i]
        bossid = i

#MARK ALL CRIMINALS WHO SENT MONEY TO THE BOSS
iscriminal = [False]*100
iscriminal[bossid] = True
for i in range(numberoftransactions):
    if tolist[i] == bossid:
        iscriminal[fromlist[i]] = True

#CALCULATE BALANCES FROM ALL TRANSACTIONS FOR EVERYONE
balance = [0]*100
for i in range(numberoftransactions):
    balance[tolist[i]] += amountlist[i]
    balance[fromlist[i]] -= amountlist[i]

#WRITE REPORT ONLY PRINT CRIMINALS (NATURALLY SORTED BECAUSE WE LOOP INDEXES FROM 0 TO 99)
report = open("analysis.txt", "w")
report.write("id\tname\tbalance\n")
for i in range(100):
    if iscriminal[i] == True:
        report.write(f"{i}\t{names[i]}\t{balance[i]}\n")

report.close()
