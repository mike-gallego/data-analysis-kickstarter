# Import our main module
from Kickstarter import Kickstarter

# We are dealing with arrays so this will be handy
import numpy as np

# We want to display the user some graphical analysis
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create a kickstarter object
df = Kickstarter('success rate of kickstarters',
                 col_list=['deadline', 'launched', 'state', 'usd_pledged_real', 'usd_goal_real'])

# Shortening df.data to just data. We are assigning it to the numpy array
data = df.data

# Outputting the total number of kickstarters for 2017
print(
    '\n' + 'Out of a total of {:,} kickstarter projects for 2017, here are some stats about its success rate:\n'.format(
        len(data)))

# These are placeholders that will hold counters of states the company was in
number_of_successes = 0
number_of_failures = 0
number_of_cancellations = 0
number_of_live = 0

# Here we want to iterate through the data list with column state
for state in data[:, 2]:
    if state == 'successful':
        number_of_successes += 1
    elif state == 'failed':
        number_of_failures += 1
    elif state == 'canceled':
        number_of_cancellations += 1
    else:
        number_of_live += 1

# Output the counter of each state
print('Success overall: {:,}'.format(number_of_successes))
print('Failures overall: {:,}'.format(number_of_failures))
print('Cancellations overall: {:,}'.format(number_of_cancellations) + '')
print('Live overall: {:,}'.format(number_of_live) + '\n')

# We want to find the success rate by dividing the number of successes to number of failures/cancellations
success_rate_with_cancellations = (round(number_of_successes / len(data) * 100, 2))
success_rate_without_cancellations = (round(number_of_successes / (number_of_successes + number_of_failures) * 100, 2))

print('The percentage of successes with cancellations overall is: {}%'.format(success_rate_with_cancellations))
print('The percentage of successes without cancellations overall is: {}%'.format(
    success_rate_without_cancellations) + '\n')

# Now maybe we can narrow it down a little more by questioning:
# What if we find the success rate of companies with small goals in mind, around 5000 or less
# Compared to the success rate of medium goals in mind, around 5000 to 20000
# Compared to the success rate of companies with big goals in mind, around 20000 or more


# Placeholders of list to collect information to the criteria
goals_5000_or_less = []
goals_5000_to_20000 = []
goals_20000_or_more = []

# Iterate through the data to put the data in the right group
for goal in data:
    if goal[-1] <= 5000:
        goals_5000_or_less.append(goal)
    elif 5000 < goal[-1] < 20000:
        goals_5000_to_20000.append(goal)
    else:
        goals_20000_or_more.append(goal)

# Change the lists to numpy arrays. Might not be necessary
goals_5000_or_less = np.array(goals_5000_or_less)
goals_5000_to_20000 = np.array(goals_5000_to_20000)
goals_20000_or_more = np.array(goals_20000_or_more)

# Outputting the length of each group to see how much there are
print('There are {:,} kickstarter projects whose goal is to meet $5,000 or less'.format(len(goals_5000_or_less)))
print('There are {:,} kickstarter projects whose goal is to meet between $5,000 and $20,000'.format(
    len(goals_5000_to_20000)))
print('There are {:,} kickstarter projects whose goal is to meet $20,000 or more \n'.format(len(goals_20000_or_more)))

# Placeholders for groups of goals and its states
success_5000_or_less = 0
failure_5000_or_less = 0
cancellation_5000_or_less = 0

success_5000_to_20000 = 0
failure_5000_to_20000 = 0
cancellation_5000_to_20000 = 0

success_20000_or_more = 0
failure_20000_or_more = 0
cancellation_20000_or_more = 0

for state in goals_5000_or_less[:, 2]:
    if state == 'successful':
        success_5000_or_less += 1
    elif state == 'failed':
        failure_5000_or_less += 1
    else:
        cancellation_5000_or_less += 1

for state in goals_5000_to_20000[:, 2]:
    if state == 'successful':
        success_5000_to_20000 += 1
    elif state == 'failed':
        failure_5000_to_20000 += 1
    else:
        cancellation_5000_to_20000 += 1

for state in goals_20000_or_more[:, 2]:
    if state == 'successful':
        success_20000_or_more += 1
    elif state == 'failed':
        failure_20000_or_more += 1
    else:
        cancellation_20000_or_more += 1

# Outputting the number of successes, failures and cancellations of kickstarters with goals $5,000 or less
print('Successes of goals $5,000 or less: {:,}'.format(success_5000_or_less))
print('Failures of goals $5,000 or less: {:,}'.format(failure_5000_or_less))
print('Cancellations of goals $5,000 or less: {:,}'.format(cancellation_5000_or_less) + '\n')

# Calculating the success rate by dividing number of successes by failures and cancellations
success_rate_5000_or_less_with_cancellations = round(
    success_5000_or_less / (success_5000_or_less + failure_5000_or_less + cancellation_5000_or_less) * 100, 2)
success_rate_5000_or_less_without_cancellations = round(success_5000_or_less / (success_5000_or_less + failure_5000_or_less) * 100, 2)
print('The success rate of kickstarters whose goal is $5,000 or less with cancellations is: {}%'.format(
    success_rate_5000_or_less_with_cancellations))
print('The success rate of kickstarters whose goal is $5,000 or less without cancellations is: {}%'.format(
    success_rate_5000_or_less_without_cancellations) + '\n')

# Outputting the number of successes, failures and cancellations of kickstarters with goals $5,000 to $20,0000
print('Successes of goals $5,000 to $20,000: {:,}'.format(success_5000_to_20000))
print('Failures of goals $5,000 to $20,000: {:,}'.format(failure_5000_to_20000))
print('Cancellations of goals $5,000 to $20,000: {:,}'.format(cancellation_5000_to_20000) + '\n')

# Calculating the success rate by dividing number of successes by failures and cancellations
success_rate_5000_to_20000_with_cancellations = round(
    success_5000_to_20000 / (success_5000_to_20000 + failure_5000_to_20000 + cancellation_5000_to_20000) * 100, 2)
success_rate_5000_to_20000_without_cancellations = round(success_5000_to_20000 / (success_5000_to_20000 + failure_5000_to_20000) * 100, 2)
print('The success rate of kickstarters whose goal is between $5,000 to $20,000 with cancellations is: {}%'.format(
    success_rate_5000_to_20000_with_cancellations))
print('The success rate of kickstarters whose goal is between $5,000 to $20,000 without cancellations is: {}%'.format(
    success_rate_5000_to_20000_without_cancellations) + '\n')

# Outputting the number of successes, failures and cancellations of kickstarters with goals $20,000 or more
print('Successes of goals $20,000 or more: {:,}'.format(success_20000_or_more))
print('Failures of goals $20,000 or more: {:,}'.format(failure_20000_or_more))
print('Cancellations of goals $20,000 or more: {:,}'.format(cancellation_20000_or_more) + '\n')

# Calculating the success rate by dividing number of successes by failures and cancellations
success_rate_20000_or_more_with_cancellations = round(
    success_20000_or_more / (success_20000_or_more + failure_20000_or_more + cancellation_20000_or_more) * 100, 2)
success_rate_20000_or_more_without_cancellations = round(success_20000_or_more / (success_20000_or_more + failure_20000_or_more) * 100, 2)
print('The success rate of kickstarters whose goal is $20,000 or more with cancellations is: {}%'.format(
    success_rate_20000_or_more_with_cancellations))
print('The success rate of kickstarters whose goal is $20,000 or more without cancellations is: {}%'.format(
    success_rate_20000_or_more_without_cancellations) + '\n')

# Make graph of the data by having a dictionary of size of goals

# First we want to create a dictionary of x and y values, where x is the name of the groups, and y is the percentages
group_of_goals = {'Overall':
                      success_rate_with_cancellations,
                  '$5000 or less':
                      success_rate_5000_or_less_with_cancellations,
                  '$5000 to 20000':
                      success_rate_5000_to_20000_with_cancellations,
                  '$20000 or more':
                      success_rate_20000_or_more_with_cancellations}

group_of_goals_without_cancellation = {'Overall':
                                           success_rate_without_cancellations,
                                       '$5000 or less':
                                           success_rate_5000_or_less_without_cancellations,
                                       '$5000 to $20000':
                                           success_rate_5000_to_20000_without_cancellations,
                                       '$20000 or more':
                                           success_rate_20000_or_more_without_cancellations}

# Setting up the bar graph
index = np.arange(4)
bar_width = 0.35

# Plotting the bar graph with two sets of values. One with cancellation and one without cancellation
rects1 = plt.bar(index, list(group_of_goals.values()), bar_width,
                 color='b',
                 label='With Cancellation')

rects2 = plt.bar(index + bar_width, list(group_of_goals_without_cancellation.values()), bar_width,
                 color='g',
                 label='Without Cancellation')

# These are the ticks for the groups
plt.xticks(range(len(group_of_goals)), list(group_of_goals.keys()))

# Setting the labels and titles
plt.xlabel('Group of Goals')
plt.ylabel('Success Rate')
plt.title('Success Rates of Kickstarter Projects 2015 - Today')

# Setting the legend to match the different types of groups
plt.legend(['With Cancellation', 'Without Cancellation'])


# Show the graph
plt.show()
