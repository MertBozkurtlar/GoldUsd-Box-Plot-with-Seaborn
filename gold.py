import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Import gold file from yahoo finance
gold = pd.read_csv('gold.csv', index_col='Date')
gold = gold.drop(['Volume'], axis=1)
gold = gold.replace(0, np.nan)
gold = gold.dropna()

WayList = gold['Close'].subtract(gold['Open']) >= 0

# Plotting with seaborn
plot = sns.catplot(kind='box', data=gold.T)
plot.fig.suptitle('GoldUsd Chart')
plot.set(xlabel='Date', ylabel='Price (USD)')
plt.xticks(rotation=90, fontsize=7, fontname='times')

# Coloring
boxes = plot.ax.artists
for i in range(len(boxes) - 1):
    if WayList[i]:
        boxes[i].set_facecolor('#add8e6')
    else:
        boxes[i].set_facecolor('Red')

plot = plt.show()
