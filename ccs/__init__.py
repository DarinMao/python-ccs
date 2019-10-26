import requests
from bs4 import BeautifulSoup

from .image import Image
from .team import Team
from .teamsummary import TeamSummary

### DIVISIONS ################################################################
MIDDLE_SCHOOL = "Middle School"
MS = MIDDLE_SCHOOL
HIGH_SCHOOL = "High School"
HS = HIGH_SCHOOL
OPEN = "Open"
ALL_SERVICE = "All Service"
AS = ALL_SERVICE

### SORTS ####################################################################
TEAM_NUMBER = "Number"
NUMBER = TEAM_NUMBER
LOCATION_CATEGORY = "Location"
LOCATION = LOCATION_CATEGORY
CATEGORY = LOCATION_CATEGORY
SCORED_IMAGES = "Images"
IMAGES = SCORED_IMAGES
PLAY_TIME = "Received"
TIME = PLAY_TIME
WARNING = "Warning"
WARN = WARNING
CCS_SCORE = "Score"
SCORE = CCS_SCORE

def scoreboard(division="", sort=""):
   p = (("division", division), ("sort", sort))
   r = requests.get("http://scoreboard.uscyberpatriot.org/",
      params=p)
   r.raise_for_status()
   soup = BeautifulSoup(r.content, "html.parser")
   teams = []
   for row in soup.find_all("tr", {"class": "clickable"}):
      cols = [c.text for c in row.find_all("td")]
      team = TeamSummary(cols[1], cols[2], cols[3], cols[5], 
            cols[6], None, cols[7], int(cols[8]))
      teams.append(team)
   return teams

def team(number):
   p = (("team", number),)
   r = requests.get("http://scoreboard.uscyberpatriot.org/team.php",
      params=p)
   if r.history:
      raise ValueError("Invalid team number")
   r.raise_for_status() 
   soup = BeautifulSoup(r.content, "html.parser")
   tables = soup.find_all("table", {"class": "CSSTableGenerator"})
   cols = [c.text for c in tables[0].find_all("tr")[1].find_all("td")]
   summary = TeamSummary(cols[0], cols[1], cols[2], cols[4], cols[5], 
         cols[6], cols[7], cols[8])
   images = []
   for row in tables[1].find_all("tr")[1:]:
      cols = [c.text for c in row.find_all("td")]
      image = Image(cols[0], cols[1].lstrip(), int(cols[2]), int(cols[3]), 
            int(cols[4]), int(cols[5]), cols[6])
      images.append(image)
   return Team(summary, images)