import subprocess
import sys
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


address = sys.argv[1]
print(address, f'git --git-dir {address}.git log')

res = subprocess.check_output(f'git --git-dir {address}.git log --pretty=format:"%ad" ', universal_newlines=True)

date = {}

timeline = np.zeros((7, 53))
commit = np.zeros((7, 24))

i = 0
for line in res.splitlines():
    date[i] = datetime.strptime(line, '%a %b %d %X %Y %z')

    calendar = date[i].isocalendar()

    timeline[calendar[2] -1][calendar[1] - 1] += 1
    commit[calendar[2] -1][date[i].hour] += 1

    i += 1


days = ['Mon', '', 'Wed', '', 'Fri', '', 'Sun']
months =  ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan']

fig_timeline, _ = plt.subplots()

plt.imshow(timeline)

arrangedMonths = []
y = -1
for i, month in enumerate(months):
    monthAdded = False
    while monthAdded is False:
        if y % 12 == 0:
            arrangedMonths.append('')
        if y % 4 == 0:
            arrangedMonths.append(months[i])
            monthAdded = True
        else:
            arrangedMonths.append('')
        y += 1

plt.xlabel('Weeks')
plt.ylabel('Days')
plt.xticks(np.arange(0, 53, 1.0), arrangedMonths)
plt.yticks(np.arange(0, 7, 1.0), days)

fig_timeline.savefig('timeline.png')

xCoord = []
yCoord = []
dotSize = []

fig_commits, ax = plt.subplots()

for i in range(len(commit)):
    for j in range(len(commit[i])):
        xCoord.append(i)
        yCoord.append(j)
        dotSize.append(commit[i, j] * 5 )

im = ax.scatter(xCoord, yCoord, dotSize)

hours =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23' ]

plt.xlabel('Days')
plt.ylabel('Hours')
plt.xticks(np.arange(0, 7, 1.0), days)
plt.yticks(np.arange(0, 24, 1.0), hours)
plt.gca().invert_yaxis()

fig_commits.savefig('commit.png')
