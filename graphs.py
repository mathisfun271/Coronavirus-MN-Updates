#Covid Updates!

import matplotlib.pyplot as plt
import numpy as np

dataAr = open("covid/graphData.txt","r").read().split("\n")

x = []
deaths = []
hosp = []
cases = []
tests = []

posP = []
deathP = []

for el in dataAr:
    ar = el.split("\t")
    x.append(int(ar[1]))
    cases.append(int(ar[2]))
    hosp.append(int(ar[3]))
    deaths.append(int(ar[4]))
    tests.append(int(ar[5]))
    posP.append(float(ar[6].replace("%","")))
    deathP.append(float(ar[7].replace("%","")))

y1, y2, y3, y4 = [],[],[],[]

for n in x:
    y1.append(deaths[n])
    y2.append(hosp[n]-deaths[n])
    y3.append(cases[n]-hosp[n])
    y4.append(tests[n]-cases[n])

labels = ["Deaths", "Hospitalizations", "Cases"]

fig, ax = plt.subplots() #linear Render
ax.stackplot(x, y1, y2, y3, labels=labels)
ax.legend(loc='upper left')
ax.set_xlabel('Days since index case, March 6th')
ax.set_ylabel('confirmed count')
plt.title('Linear Graph')
fig.savefig('covid/linGraph.png')

labels.append("Tests")
fig, ax = plt.subplots() #Logarithmic Render
ax.stackplot(x, y1, y2, y3, y4, labels=labels)
ax.legend(loc='upper left')
plt.title('Logarithmic Graph')
ax.set_yscale('log')
ax.set_ylabel('confirmed count')
ax.set_xlabel('Days since index case, March 6th')
fig.savefig('covid/logGraph.png')

fig, ax = plt.subplots() #Logarithmic Render
ax.plot(posP, label= "% Positive Tests")
ax.plot(deathP, label="% Fatality")
ax.legend(loc='upper left')
ax.set_xlabel('Days since index case, March 6th')
ax.set_ylabel('Percentage')
plt.title('Percentage Graph')
fig.savefig('covid/percentGraph.png')


