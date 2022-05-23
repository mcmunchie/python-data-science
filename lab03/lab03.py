'''
Code Summary: This source code file demonstrates data analysis using Pandas library and CDC COVID statistics. 

List of resources
Understanding COVID-19 Dataset
https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36
https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36/data

Working with Pandas
https://pandas.pydata.org/docs/user_guide/missing_data.html
https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.strftime.html
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''

from datetime import date, timezone
import datetime
from io import StringIO
import pandas as pd
import requests

'''
NOTE(S): Will need to install Jinja2 in order to process data output file. 
Missing data in historic cases (do not know how to calculate). Timezone is not printing correctly (missing hour:minute:second status, as well as timezone.) Minor formatting issues.
'''

def national_summary(df: pd.DataFrame):
  '''
  Display national summary of all states of the following categories: total_cases, total_new_cases, total_deaths, total_new_deaths. First fetch the national stats, then format print each result.
  '''
  print('\n\tNational Summary (all states):\n')

  total_cases = df['tot_cases'].sum()
  total_new_cases = df['new_case'].sum()
  total_death = df['tot_death'].sum()
  total_new_death = df['new_death'].sum()

  print('\t\tTotal Cases: {}'.format(total_cases))
  print('\t\tTotal New Cases: {}'.format(total_new_cases))
  print('\t\tTotal Deaths: {}'.format(total_death))
  print('\t\tTotal New Deaths: {}'.format(total_new_death))

  print('\n\t...National summary has finished.')

  
def state_summary(df: pd.DataFrame):
  '''
  Display state summary based on user input (user should enter a two-character state code). State summary should display information about the following categories: total_cases, total_new_cases, total_deaths, total_new_deaths. First fetch selected state summary data based on state code, then format print each result. Check if entered state code is valid.
  '''
  state = input('\n\tPlease enter a state (2-letter state code): ').upper()
  
  try: # does not catch properly, should put inside a while loop for validation check (int, single letter cases)
    df = df.loc[df['state'] == state]
  except ValueError:
    print('Invalid input. Please try again.')
    return False

  print('\n\tState Summary:\n')

  total_cases = df['tot_cases'].sum()
  total_new_cases = df['new_case'].sum()
  total_death = df['tot_death'].sum()
  total_new_death = df['new_death'].sum()

  print('\t\tTotal Cases: {}'.format(total_cases))
  print('\t\tTotal New Cases: {}'.format(total_new_cases))
  print('\t\tTotal Deaths: {}'.format(total_death))
  print('\t\tTotal New Deaths: {}'.format(total_new_death))

  print('\n\t...State summary for {} has finished.'.format(state))

  return True


def data_analysis(df: pd.DataFrame):
  '''
  Display the top number of states by summary statistics (total_cases, total_new_cases, total_deaths, total_new_deaths), based on user input. 
  '''
  user = input('\n\tPlease enter a number for the top number of states: ')

  try:
    user = int(user)
  except ValueError:
    print('Invalid input. Please try again.')
    return False

  print('\n\tHere are the top {} states for the following categories: '.format(user))

  states = df.groupby('state')

  total_cases = states['tot_cases'].sum().sort_values(ascending=False)
  total_new_cases = states['new_case'].sum().sort_values(ascending=False)
  total_death = states['tot_death'].sum().sort_values(ascending=False)
  total_new_death = states['new_death'].sum().sort_values(ascending=False)

  print('\n\tTotal Cases: ')
  print(total_cases.head(user))
  
  print('\n\tTotal New Cases: ')
  print(total_new_cases.head(user))
  
  print('\n\tTotal Deaths: ')
  print(total_death.head(user))

  print('\n\tTotal New Deaths: ')
  print(total_new_death.head(user))

  print('\n\t...Data analysis has finished.')

  return True


def data_output(df: pd.DataFrame):
  '''
  Process and output data into a new output file, similar to the COVID data file from lab 2. Create new columns for the 7 day averages and historic cases, set to zero. Rename columns to resemble lab 2 csv file. Figure out how to calculate historic and 7 day averages columns. Format date column and write row information to new output file. Format output to match original csv file.
  '''
  print('\n\t...Writing data to \'data_output.csv\'...')

  df['7-Day Moving Avg'] = 0
  df['Historic Cases'] = 0

  df = df[['state', 'submission_date', 'new_case', '7-Day Moving Avg', 'Historic Cases']].sort_values (by='submission_date')

  df.rename(columns={'state': 'State', 'submission_date': 'Date', 'new_case': 'New Cases'}, inplace=True)

  df['7-Day Moving Avg'] = df.apply(lambda row: round(df['New Cases'][row.name:row.name + 7].mean()), axis=1)

  # df['Historic Cases'] = df.apply(lambda row: round(df[''])) # how to calculate this???

  df['Date'] = pd.to_datetime(df['Date']).apply(lambda date: date.strftime('%b %d %Y'))

  with open('lab03\data_output.csv', 'w') as outfile:
    today = date.today()
    timezone = datetime.datetime.utcnow().astimezone().tzinfo
    outfile.write('Data Table for Daily Case Trends - The United States\n')
    outfile.write('Date generated: ' + today.strftime('%a %b %d %Y %X'))
    outfile.write('(' + str(timezone) + ')\n')

  df.style.format('%20s')

  df.to_csv('lab03\data_output.csv', index=False, mode='a')
  
  print('\n\t...Finished processing the file.')


def user_options():
  '''
  Create user-friendly menu to navigate program.
  '''
  print('\n')
  print('\t[0] Exit the program.')
  print('\t[1] Display national summary.')
  print('\t[2] Display a state summary.')
  print('\t[3] Display a data analysis of the top states for each statistical category.')
  print('\t[4] Process and output data into a csv file.\n')

  option = input('Please choose a function to run (enter number): ')

  return option


def main():
  '''
  Main method for running the lab module.
  '''
  print('Hi! Welcome to Lab 3.\n')
  print('\n\tRetrieving data...\n')
  url = requests.get('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD')
  df = pd.read_csv(StringIO(url.text))

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
      national_summary(df)
    elif option == 2:
      state_summary(df)
    elif option == 3:
      data_analysis(df)
    elif option == 4:
      data_output(df)
    elif option == 0:
      break
    
    user = input('\nWould you like to run another function? (Y/N): ')
    print()

  print('Thank you.')


if __name__ == "__main__":
  main()
