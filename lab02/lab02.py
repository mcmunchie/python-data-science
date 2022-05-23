'''
Code Summary: This lab demonstrates data manipulation using a CSV file from the CDC database.

List of resources
Understanding COVID-19 Dataset
https://covid.cdc.gov/covid-data-tracker/#trends_dailycases

Working with Pandas
https://pandas.pydata.org/docs/user_guide/index.html

Working with Matplotlib/Visualization
https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/
https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
'''

from os.path import exists
import pandas as pd
import csv
import matplotlib.pyplot as plt

def duplicate_data(input_file, output_file):
  '''
  Duplicate the original file's data into an output csv file, and save it into the project directory.
  Opens and reads from an input file and writes into an output file. Reader object used to read from the input file and writer object used to copy all data from the input file into the output file (using a delimiter to separate
  file contents). Writer iterates over each row in the input file and appends the file information to the data list.

  Returns the list containing the duplicated data.
  '''
  data = []
  with open(input_file) as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter=',')

    for row in reader:
      writer.writerow(row)
      data.append(row)

  print('\t...File was duplicated to duplicate.csv')

  return data


def copy_data(input_file, output_file):
  '''
  Copy data from the original file (skipping rows that do not contain actual data) into an output file.
  Assigns header to second row by index and skips over the first three rows. Uses pandas module to read input file
  as a pandas dataframe and copies the original data into the output file as a csv file.
  '''
  df = pd.read_csv(input_file, header = 2)
  df.to_csv(output_file, header = False)

  print('\t...The data from the original file was copied to copy_data.csv')


def display_title(input_file):
  '''
  Extract and display the file title.
  Opens file and assigns title to next(infile), but returns only the title row.
  Prints the file title and encoding utf-8-sig removes special characters from the beginning of the row.
  '''
  with open(input_file, encoding = 'utf-8-sig') as infile:
    title = next(infile)
    print(title, end = '')
  
  print('\n\t...File title was displayed.')


def display_generation(input_file):
  '''
  Extract and display the file generation/run-date.
  Opens file and uses next to iterate over file title until file generation row is reached.
  Prints the file generation/run-date from index 1 (or the next row after title). 
  '''
  with open(input_file) as infile:
    title = next(infile)
    run_date = next(infile)
    print(run_date, end = '')

  print('\n\t...File generation/run-date was displayed.')


def display_col_names(input_file):
  '''
  Extract and display the column names as a list.
  Opens file and uses a counter to iterate through each line until line 3 (index 2) is reached.
  Returns a copy of the line with whitespace removed, and separates each list value with a comma.
  '''
  with open(input_file) as infile:
    count = 0
    while (count <= 2):
      line = next(infile)

      if (count == 2):
        print([col.strip() for col in line.split(',')])

      count += 1

  print('\n\t...Row column names was displayed.')


def display_data(input_file):
  '''
  Extract and display data from file as a list of lists.
  Reads input file as a pandas dataframe, ignoring the header (indexes 0,1,2).
  Prints dataframe values as a list of lists.
  '''
  df = pd.read_csv(input_file, header = 2)
  print(df.values)

  print('\n\t...File data as a list was displayed.')


def display_recent_days(input_file):
  '''
  Extract and display the most recent five days of data.
  Reads in file as a dataframe, ignoring the first few lines. Prints the head (first five values) of the dataframe, using the 'Date' and 'New Cases' labels.
  '''
  print('The Five Most Recent Cases:\n')
  df = pd.read_csv(input_file, header = 2)
  print(df.head()[['Date', 'New Cases']])

  print('\n\t...The most recent five days of data was displayed.')


def get_highest_cases(input_file):
  '''
  Extract and display the highest number of cases on a single day.
  Uses a dataframe to extract values based on the 'New Cases' label, and returns the maximum value from this column.
  '''
  df = pd.read_csv(input_file, header = 2)
  print('The Highest Number of Cases on a Single Day:\n')
  print('New Cases: ', end = '')
  print(df['New Cases'].max())

  print('\n\t...The highest number of cases on a single day was displayed.')


def ten_highest_days(input_file):
  '''
  Extract and display the highest ten days of cases.
  Uses a dataframe to sort values by 'New Cases', and filters the highest value based on the corresponding 'Date'.
  Returns and prints the maximum value as a string.
  '''
  df = pd.read_csv(input_file, header = 2)

  print('The Highest Ten Days of Cases:\n')
  print(df.sort_values(by='New Cases', ascending = False)
        [0:9][['Date', 'New Cases']].to_string(index = False))

  print('\n\t...The highest ten days of cases was displayed.')


def monthly_summary(input_file):
  '''
  Extract and display a summary of each month of data provided, in a formatted display.
  '''
  df = pd.read_csv(input_file, header = 2, index_col = False)
  df = df.rename(columns={'Date': 'Month'}) # rename 'Date' column to 'Month'

  # Convert data column to datetime objects
  df['Month'] = pd.to_datetime(df['Month'])
  # Format to month(s) only
  df['Month'] = df['Month'].apply(
    lambda data: data.strftime('%b'))

  # Create counts Series
  cts = pd.DataFrame()
  cts['Count'] = 1
  cts['Count'] = df.groupby('Month')['New Cases'].count()

  # Create averages Series
  avgs = pd.DataFrame()
  avgs['Average Cases'] = 1
  avgs['Average Cases'] = df.groupby('Month')['New Cases'].mean()

  # Merge averages and counts
  months = pd.merge(cts, avgs, on='Month')

  # List months in order
  months = months.reindex(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

  print(months)

  print('\n\t...The summary of each month was displayed.')


def visualize_data(input_file):
  '''
  Display summary of data as a bar graph, with historic cases being the y-axis and new cases being the x-axis.
  '''
  df = pd.read_csv(input_file, header = 2)
  df = df.describe()

  print('\tDisplaying graph...')

  graph = df[['New Cases', 'Historic Cases']].plot(kind='bar', title='Relationship between Historic Cases and New Cases', figsize=(10,15), legend=True, fontsize=12)
  graph.set_xlabel('New Cases', fontsize=12)
  graph.set_ylabel('Historic Cases', fontsize=12)
  plt.show()


def user_options():
  '''
  Create user-friendly menu to navigate program.
  '''
  print('\n')
  print('\t[0] Exit the program.')
  print('\t[1] Duplicate the original file.')
  print('\t[2] Copy the data from the original file.')
  print('\t[3] Display the file title.')
  print('\t[4] Display the file generation/run-date.')
  print('''\t[5] Display the file's row and column names.''')
  print('\t[6] Display data as a list.')
  print('\t[7] Display the most recent five days of data.')
  print('\t[8] Display the highest number of cases on a single day.')
  print('\t[9] Display the highest ten days of cases.')
  print('\t[10] Display a summary of each month of data provided.')
  print('\t[11] Display the summary of data in a graph.\n')

  option = input('Please choose a function to run (enter number): ')

  return option


def main():
  '''
  Main method for running the lab module.
  '''
  print('Hi! Welcome to Lab 2.\n')
  user = input('Would you like to run a function? (Y/N): ')

  while(user.lower() == 'yes' or user.lower() == 'y'):
    option = user_options()
    print()

    if (option.lower() == 'no' or option.lower() == 'n'):
      break

    try:
      option = int(option)
    except ValueError:
      print('Invalid option. Please try again.')

    if option == 1:
      if not exists('lab02\duplicate.csv'):
        duplicate_data('lab02\data_table_for_daily_case_trends__the_united_states.csv', 'lab02\duplicate.csv')
      else:
        print('The file was already duplicated into the current project directory. This file already exists as \'duplicate.csv\'.')
    elif option == 2:
      if not exists('lab02\copy_data.csv'):
        copy_data('lab02\data_table_for_daily_case_trends__the_united_states.csv', 'lab02\copy_data.csv')
      else:
        print('The file was already copied into the current project directory. This file already exists as \'copy_data.csv\'.')
    elif option == 3:
      display_title('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 4:
      display_generation('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 5:
      display_col_names('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 6:
      display_data('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 7:
      display_recent_days('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 8:
      get_highest_cases('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 9:
      ten_highest_days('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 10:
      monthly_summary('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 11:
      visualize_data('lab02\data_table_for_daily_case_trends__the_united_states.csv')
    elif option == 0:
      break
    
    user = input('\nWould you like to run another function? (Y/N): ')
    print()

  print('Thank you.')


if __name__ == "__main__":
  main()
