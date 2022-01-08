log_file = open("qgames.log")
players = []
kills = {}
count = 0

# get the name of each player for each match
for line in log_file:
    if "Kill" in line:
        # get the killer --> can be improved using regex
        killer = line.split(":")[3].strip().split()[0]        
        # print(killer)

    if "ShutdownGame" in line:
        count+=1
        print("game_%d" % count)