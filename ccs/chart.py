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