import requests
from bs4 import BeautifulSoup
import json

from .model import *
from .const import *
from .exception import *

def scoreboard(division=ALL, sort=""):
   p = (("division", division), ("sort", sort))
   r = requests.get("http://scoreboard.uscyberpatriot.org/",
      params=p)
   r.raise_for_status()
   if r.content == "":
      raise ScoreboardDownException("Scoreboard is down")
   soup = BeautifulSoup(r.content, "html.parser")
   teams = []
   for row in soup.find_all("tr", {"class": "clickable"}):
      cols = [c.text for c in row.find_all("td")]
      if len(cols) > 11:
         team = TeamSummary(cols[1], cols[2], cols[3], cols[4], int(cols[5]), 
               cols[6], None, cols[7], int(cols[8]), float(cols[9]),
               float(cols[10]), float(cols[11]))
      elif len(cols) == 11:
         team = TeamSummary(cols[1], cols[2], cols[3], cols[4], int(cols[5]), 
               cols[6], None, cols[7], int(cols[8]), float(cols[9]),
               0.0, float(cols[10]))
      else:
         team = TeamSummary(cols[1], cols[2], cols[3], cols[4], int(cols[5]), 
               cols[6], None, cols[7], int(cols[8]))
      teams.append(team)
   return teams

def team(number):
   p = (("team", number),)
   r = requests.get("http://scoreboard.uscyberpatriot.org/team.php",
      params=p)
   if r.history:
      raise NoSuchTeamException("Team does not exist on scoreboard")
   r.raise_for_status() 
   if r.content == "":
      raise ScoreboardDownException("Scoreboard is down")
   soup = BeautifulSoup(r.content, "html.parser")
   tables = soup.find_all("table", {"class": "CSSTableGenerator"})
   cols = [c.text for c in tables[0].find_all("tr")[1].find_all("td")]
   if len(cols) > 11:
      summary = TeamSummary(cols[0], cols[1], cols[2], cols[3], int(cols[4]), cols[5], 
            cols[6], cols[7], int(cols[8]), float(cols[9]), float(cols[10]), 
            float(cols[11]))
   elif len(cols) == 11:
      summary = TeamSummary(cols[0], cols[1], cols[2], cols[3], int(cols[4]), cols[5], 
            cols[6], cols[7], int(cols[8]), float(cols[9]), 0.0, 
            float(cols[10]))
   else:
      summary = TeamSummary(cols[0], cols[1], cols[2], cols[3], int(cols[4]), cols[5], 
            cols[6], cols[7], int(cols[8]))
   images = []
   for row in tables[1].find_all("tr")[1:]:
      cols = [c.text for c in row.find_all("td")]
      image = Image(cols[0], cols[1].lstrip(), int(cols[2]), int(cols[3]), 
            int(cols[4]), int(cols[5]), cols[6])
      images.append(image)
   chart_start_key = "arrayToDataTable("
   chart_start = r.content.index(chart_start_key)+len(chart_start_key)
   chart_end = r.content.index(");", chart_start)
   chart_table = r.content[chart_start:chart_end]
   chart_data = json.loads((chart_table[:chart_table.rfind(",")]+"]").replace("'", '"'))
   chart = Chart(chart_data)
   return Team(summary, images, chart)