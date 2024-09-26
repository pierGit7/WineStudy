import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wine_data_fixed.csv")
# List of headings:
headings = []
for col in df.columns:
    headings.append(col)

print(headings)

fig, axs = plt.subplots(nrows=7, ncols=2, figsize=(8,13))


for i, heading in enumerate(headings):
    row = i // 2
    col = i % 2
    
    sns.histplot(df[heading], kde=True, bins=25, ax=axs[row, col], stat="frequency") #Currently set to freq
    plt.xlabel(heading)

fig.delaxes(axs[6,1]) #Delete the odd empty plot
plt.tight_layout()
plt.subplots_adjust(hspace=0.5) # adjust vertical space between plots
plt.show()