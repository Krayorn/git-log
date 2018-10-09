import subprocess
import sys
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


address = sys.argv[1]
print(address, f'git --git-dir {address}.git\ log')

res = subprocess.check_output(f'git --git-dir {address}.git\ log --pretty=format:"%ad" ', universal_newlines=True)

date = {}

timeline = np.zeros((53, 7))
commit = np.zeros((7, 24))

i = 0
for line in res.splitlines():
    date[i] = datetime.strptime(line, '%a %b %d %X %Y %z')

    calendar = date[i].isocalendar()

    timeline[calendar[1]][calendar[2] -1 ] += 1
    commit[calendar[2] -1][date[i].hour] += 1

    i += 1


fig, ax = plt.subplots(1, 1)

plt.imshow(timeline)
fig.savefig('timeline.png')

plt.imshow(commit)
fig.savefig('commit.png')
