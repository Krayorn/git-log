import subprocess
import sys
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


address = sys.argv[1]
print(address, f'git --git-dir {address}.git\ log')

res = subprocess.check_output(f'git -C {address}.git\ log --pretty=format:"%ad" ', universal_newlines=True)

date = {}

timeline = np.zeros((53, 7))

i = 0
for line in res.splitlines():
    date[i] = datetime.strptime(line, '%a %b %d %X %Y %z')
    timeline[date[i].isocalendar()[1]][date[i].isocalendar()[2] -1 ] += 1
    i += 1


fig, ax = plt.subplots(1, 1)

plt.imshow(timeline)

fig.savefig('timeline.png')
