# import dependencies
import matplotlib.pyplot as plt
import csv
import itertools

# read the data from csv file
with open('irisData.csv', 'r', encoding='UTF-8') as f:
    data = csv.reader(f)
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    for i in data:
        c1.append(float(i[0]))
        c2.append(float(i[1]))
        c3.append(float(i[2]))
        c4.append(float(i[3]))
dataSet = [c1, c2, c3, c4]

possiblePairs = list(itertools.combinations(range(0,4), 2))

plt.style.use('fivethirtyeight')
figs, ax = plt.subplots(nrows=2, ncols=3, figsize=(20,12))
# figs.subplots_adjust(hspace=.5)
subplots = []
for row in ax:
    for col in row:
        subplots.append(col)

for i in range(len(possiblePairs)):
    p = possiblePairs[i]
    subP = subplots[i]
    subP.scatter(dataSet[p[0]][0:50],dataSet[p[1]][0:50], c = "green", linewidths = 1, marker = "s", edgecolor = "green", s = 20)
    subP.scatter(dataSet[p[0]][50:100],dataSet[p[1]][50:100], c = "red", linewidths = 1, marker = "^", edgecolor = "red", s = 20)
    subP.scatter(dataSet[p[0]][100:150],dataSet[p[1]][100:150], c = "blue", linewidths = 1, marker = "o", edgecolor = "blue", s = 20)
    subP.set_title('Property {} vs Property {}'.format(p[0]+1, p[1]+1), fontsize=12)

# save the plot
plt.savefig('comparison.png')
plt.show()





