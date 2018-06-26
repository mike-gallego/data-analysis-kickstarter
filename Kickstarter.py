import numpy as np
import pandas as pd


class Kickstarter():
    def __init__(self, tag, col_list=[]):

        # We create a tag so that we know what our project is going to be about
        self.tag = tag
        # We create a column list because if the user wants specific columns instead of everything, it will be possible
        self.col_list = col_list

        # We are going to use this placeholder so that the user can view the columns in an array
        self.columns = []

        # If the user doesn't want to specify columns, the condition will return true
        if len(self.col_list) == 0:

            # Assigning df to the csv file
            df = pd.read_csv('kickstarter_2018.csv', encoding='utf-8')

            # We are assigning our data with type numpy array to the csv data using pandas
            self.data = np.array(df)

            # Our columns is a list of the first row
            self.columns = df.columns.values.tolist()
        else:

            self.df = pd.read_csv('kickstarter_2018.csv', encoding='utf-8', usecols=col_list)
            # We are assigning our data with type numpy array to the csv data using pandas

            self.data = np.array(self.df)
            self.columns = self.df.columns.values.tolist()

    # When user prints object, this string will return
    def __str__(self):
        return 'This data is going to about the ' + str(self.tag) + '.'
