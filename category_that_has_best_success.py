import numpy as np
from Kickstarter import Kickstarter
from collections import Counter
import matplotlib.pyplot as plt

# From our Kickstarter we will create an object to proccess data easier
df = Kickstarter('The Category that has the best success rate overall', ['main_category', 'state'])

# Assign data to our dj object's numpy data
data = df.data.tolist()

# This will be very easy. We will have two placeholders: success and failure
success = 0
failure = 0

# We need a dictionary to put state values to the corresponding keys
categories = {}

# First we have to iterate through the data to put values and keys into the dictionary
for row in data:
    if row[0] not in categories:
        categories[row[0]] = [row[1]]
    else:
        categories[row[0]] += [row[1]]

# Output a clear list of keys for guidance
print(categories.keys())

# Iterate through categories to collect states to the right keys
for k, v in categories.items():
    if categories[k]:
        c = Counter(categories[k])
        categories[k] = round(c['successful'] / (c['successful'] + c['failed']) * 100, 2)

# Sort dictionary by value
categories = sorted(categories.items(), key=lambda x: -x[1])
print(categories)

y_rate = []
x_category = []

for row in categories:
    x_category.append(row[0])
    y_rate.append(row[1])

print(x_category)
print(y_rate)

plt.bar(x_category, y_rate)

plt.xlabel('Categories')
plt.ylabel('Success Rate')

plt.title('Categories from Most Successful to Least Successful')

plt.show()
