import ccs

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.rcParams["toolbar"] = "None"

team = ccs.team(raw_input("Team Number: "))
chart = team.chart

fig, ax = plt.subplots()

for k in range(len(chart.images)):
   plt.plot(chart.timestamps, chart.scores[k], 
         label=chart.images[k])

plt.title(team.summary.number + " Image Scores")
plt.legend()
xlocator = mdates.MinuteLocator(byminute=[0, 15, 30, 45], interval=1)
xformat = mdates.DateFormatter("%m/%d %H:%M")
ax.xaxis.set_major_locator(xlocator)
ax.xaxis.set_major_formatter(xformat)
fig.autofmt_xdate()
plt.show()