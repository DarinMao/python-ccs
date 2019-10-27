# python-ccs
Python wrapper for online CyberPatriot scoreboard

## Installation
```
$ git clone https://github.com/DarinMao/python-ccs/
$ cd python-ccs
$ pip install .
```

## Methods
### scoreboard(division, sort)
This method returns a list of [TeamSummary](#teamsummary) objects
#### Parameters
* `division` can be any of these
```
ccs.MIDDLE_SCHOOL
ccs.MS

ccs.HIGH_SCHOOL
ccs.HS

ccs.OPEN

ccs.ALL_SERVICE
ccs.AS
```
* `sort` can be any of these
```
ccs.TEAM_NUMBER
ccs.NUMBER

ccs.LOCATION_CATEGORY
ccs.LOCATION
ccs.CATEGORY

ccs.SCORED_IMAGES
ccs.IMAGES

ccs.PLAY_TIME
ccs.TIME

ccs.WARNING
ccs.WARN

ccs.CCS_SCORE
ccs.SCORE
```

### team(number)
This method returns a [Team](#team) object describing the specified team
#### Parameters
* `number` - the team number as a string `XX-XXXX`

## Classes
### Image
This class represents a single CCS Image
#### Properties
* `name` - the name of the image
* `time` - the amount of time spent on the image
* `found` - the amount of vulnerabilities found on the image
* `remaining` - the amount of vulnerabilities remaining on the image
* `penalties` - the amount of penalties assigned to the image
* `score` - the current CCS score of the image
* `warn` - any warnings assigned to the image

### Team
This class represents a team as a combination of its summary and list of images
#### Properties
* `summary` - a [TeamSummary](#teamsummary) object representing the team
* `images` - a list of [Image](#image) objects for the team
* `chart` - a [Chart](#chart) object with the team scores per image over time

### TeamSummary
This class represents a summary of a team
#### Properties
* `number` - the team number as a string `XX-XXXX`
* `location` - the location/category of the team
* `division` - the division of the team
* `images` - the number of scored images
* `playtime` - the play time of the team
* `scoretime` - the score time of the team
* `warn` - any warnings assigned to the team
* `score` - the current CCS score of the image

### Chart
This class represents the score chart of a team
#### Properties
* `data` - the raw chart data in the form of a table
* `images` - the names of the images
* `timestamps` - the horizontal axis timestamps
* `scores` - a list of the scores over time (`scores[k]` contains the scores for `images[k]`; the graph for `images[k]` is defined by `(x, y) = (timestamps, scores[k])`)