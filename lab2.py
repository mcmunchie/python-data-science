from os.path import exists
from turtle import title
import pandas as pd
import csv
import matplotlib.pyplot as plt

# Code Summary: This lab demonstrates data manipulation using a CSV file from the CDC database.

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
