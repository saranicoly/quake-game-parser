# open files
log_file = open("qgames.log")
output_file = open("output.txt", "w")

count = 0
kills_count = 0

for line in log_file:
    if "InitGame" in line:
        count+=1
        output_file.write('"game_%d": {\n' % count)
        output_file.write('"total_kills": %d,\n' % kills_count)
        # reinitialize variables
        kills_count = 0
        players = []
        kills = {}

    if "Kill" in line:
        kills_count += 1
        # get the killer --> can be improved using regex
        killer = line.split(":")[3].strip().split()[0]        
        # print(killer)