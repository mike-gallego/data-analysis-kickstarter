from Kickstarter import Kickstarter
import numpy as np
from collections import Counter

# Create an object from Kickstarter class
df = Kickstarter('Reason why kickstarters with large goals are failing',
                 ['main_category', 'state', 'country', 'usd_pledged_real', 'usd_goal_real'])

# Description of our objective this py file
print('\n' +
      'After noticing that kickstarter projects with high goals have really low success rates, we will try to find out why')

# Placeholder for the categories in the data
categories = {}

# Placeholder of list of counter of category
category_counter_list = []

# Assign our data from kickstarter class and convert it to a list for optimal addition of lists
categories_data = df.data.tolist()

# For a simpler ease of access to data, we will group the data into dictionary keys of categories
for row in categories_data:
    if row[-1] > 20000:
        if row[0] not in categories:
            categories[row[0]] = [row[1:]]
        else:
            categories[row[0]] += [row[1:]]

        category_counter_list.append(row[0])

# Get a clear view of each category
print(categories.keys())

# Create a list for the success rates
success_rate_list = []

# Placeholder to hold tuples of category to success rate
category_success_rate = []
category_counter = 0

# Iterating through category dictionary to find the success rate of each category
for k, v in categories.items():
    if categories[k]:
        success = 0
        failed = 0
        for entry in categories[k]:

            if entry[0] == 'successful':
                success += 1
            if entry[0] == 'failed':
                failed += 1

        success_rate = round(success / (success + failed), 2)
        success_rate_list.append(success_rate)

    # Assigning the category success rate to tuples of category to success rate
    category_success_rate.append((k, success_rate_list[category_counter]))
    category_counter += 1

# Output the success rate of the list. We want to use this list to match the keys of the dictionary
print('\n{}'.format(success_rate_list))

# Output of merged categories to success rate

# Unsorted but shows list of tuples of categories to success rate
print('\n{}'.format(category_success_rate))

# Sort the list from least to greatest success rates.
category_success_rate = np.array(sorted(category_success_rate, key=lambda x: (x[1], x[0])))

# Output sorted values
print('\n{}\n'.format(category_success_rate))

# Now we see that there's a balance of low and high. Let's see the range
success_rate_list = np.array(success_rate_list)
print('The range of success rates is {}\n'.format(round(success_rate_list.max() - success_rate_list.min(), 2)))

# Lets find the mean of the success rates
print('The mean of the success rates is {}\n'.format(round(success_rate_list.mean(), 2)))

# Lets find the standard deviation to see the spread of average results
print('The standard deviation of the success rates are {}\n'.format(round(success_rate_list.std(), 2)))

# Placeholders first and second half
first_half = 0
second_half = 0

# Now we want to initiate our counter variable for the category_counter_list
c = Counter(category_counter_list)
c_list = []

# Iterate through c counter dictionary to turn it into a list of tuples of keys and values
for k, v in c.items():
    c_list.append((k, v))

c_list = np.array(c_list)

# Output the most frequent category
print('\n{}'.format(c_list))

# We will iterate through the category again to add the values to the first or second half
for row in c_list:
    if row[0] in category_success_rate[:8, 0]:
        first_half += int(row[1])
    if row[0] in category_success_rate[8:, 0]:
        second_half += int(row[1])

# Output the first and second half
print('\nThe total amount of items in the first_half of success rate of 20% and lower is {:,}'.format(first_half))
print('The total amount of items in the second_half of success rate higher than 20% is {:,}\n'.format(second_half))

# Give reasoning why kickstarter with large goals are failing
# print(
#     'The reason why kickstarters with large goals are failing is because the first half with outnumbers the second half,'
#     ' which the first half of 20% and lower success rate contains the list: \n{}\nThe second half higher than'
#     ' 20% success rate is: \n{}\nNotice how the second half is more favorable towards the arts and creativity,'
#     ' while the first half is more technical and technology related.'.format(category_success_rate[:7, 0], category_success_rate[7:, 0]))


# We want to find the success rate of the second half to see how much of a difference the success rate is
second_half_success_rate = 0

for row in category_success_rate[7:]:
    # print(type(float(row[1])))
    second_half_success_rate += float(row[1])

second_half_success_rate /= len(category_success_rate[7:])
print(second_half_success_rate)
