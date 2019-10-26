import ccs

scoreboard = ccs.scoreboard(division=ccs.MS, sort=ccs.WARN)

for team in scoreboard[:10]:
   print "Team {} ({} {}) - {} images ({} points) - {} {}".format(
      team.number, team.division, team.location, team.images, 
      team.score, team.playtime, team.warn)