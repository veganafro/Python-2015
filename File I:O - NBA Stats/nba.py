all_players = open('stats-clean.txt', 'r')
good_players = open('report.csv', 'w')

player_stats = all_players.readlines()
del player_stats[0]

for lines in player_stats:
    lines = lines.strip()
    lines = lines.split(',')
    if float(lines[5]) > 0 and (float(lines[4]) / float(lines[5])) >= 0.5:
        good_players.write("%s, %s\n" % (lines[0], (float(lines[4]) / float(lines[5]))))

all_players.close()
good_players.close()