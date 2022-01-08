# open files
log_file = open("qgames.log")
output_file = open("output.txt", "w")

# initialize variables
players = []
kills = {}
count = 0

for line in log_file:
    if "InitGame" in line:
        count+=1
        output_file.write('"game_%d": {\n' % count)
        # reinitialize variables
        players = []
        kills = {}

    if "Kill" in line:
        # get the killer --> can be improved using regex
        killer = line.split(":")[3].strip().split()[0]        
        # print(killer)