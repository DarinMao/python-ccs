import ccs

team = ccs.team(raw_input("Team Number: "))
summary = team.summary
print "Team {} ({} {}) - {} images ({} points) - {}/{} {}".format(
      summary.number, summary.division, summary.location, 
      summary.images, summary.score, summary.playtime, summary.scoretime,
      summary.warn)
for image in team.images:
   print "\t{}: {}/{} vulns in {} ({} points, {} penalties) {}".format(
         image.name, image.found, image.found+image.remaining, image.time,
         image.score, image.penalties, image.warn)