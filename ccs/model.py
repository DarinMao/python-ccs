from datetime import datetime

class Chart:
   def __init__(self, data):
      self.data = data
      self.images = data[0][1:]
      self.timestamps = []
      self.scores = [[] for image in self.images]
      for row in data[1:]:
         self.timestamps.append(datetime.strptime(row[0], "%m/%d %H:%M"))
         row = row[1:]
         for k in range(len(row)):
            self.scores[k].append(row[k])

class Image:
   def __init__(self, name, time, found, remaining, penalties, score, warn):
      self.name = name
      self.time = time
      self.found = found
      self.remaining = remaining
      self.penalties = penalties
      self.score = score
      self.warn = warn

class Team:
   def __init__(self, summary, images, chart):
      self.summary = summary
      self.images = images
      self.chart = chart

class TeamSummary:
   def __init__(self, number, location, division, images, playtime, scoretime, warn, ccs, adjust=0.0, cisco=0.0, score=None):
      self.number = number
      self.location = location
      self.division = division
      self.images = images
      self.playtime = playtime
      self.scoretime = scoretime
      self.warn = warn
      self.ccs = ccs
      self.adjust = adjust
      self.cisco = cisco
      self.score = score
      if scoretime is None:
         self.scoretime = playtime
      if score is None:
         self.score = ccs
