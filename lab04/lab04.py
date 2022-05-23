'''
Code Summary: This lab explores the various correlations of a few health conditions (i.e. bmi, physical health, mental health, sleep, and age) on the likelihood of developing heart disease. Dataset can be found here: https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease?resource=download 

Notes: Would like to narrow my focus down more to come up with a more streamline and concise data analysis of heart disease predicitions. Overall, my general insights is that a higher bmi means a person is more likely to develop heart disease, and sleep does not have that much impact on heart disease. 

Resources: https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html, https://seaborn.pydata.org/tutorial.html, https://seaborn.pydata.org/generated/seaborn.heatmap.html, https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/
'''

# import modules
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def dataAnalysis(df):
  shape = df.shape
  print("Shape: {}".format(shape))
  print("\nData Types:")
  print(df.dtypes)
  print("\nGeneral Information:")
  print(df.info())
  print("\nFirst Five Rows of Dataset:")
  print(df.head())
  print("\nBrief Description of Dataset:")
  print(df.describe())
  print("\nChecking for Missing Values:")
  print(df.isnull().sum())

def getOutliers(df, column):
  max = round(df[column].max(), 2)
  min = round(df[column].min(), 2)

  return max, min

def getSummary(df, column):
  avg = round(df[column].mean(), 2)
  values = df[["BMI", "AgeCategory", "SleepTime"]]
  # print(values.describe())
  # sum_all = round(df[["BMI", "AgeCategory", "SleepTime"]].sum(), 2)
  sum = round(df["BMI"].sum(), 2)

  return sum, avg

# what correlations are there that results in a higher change of developing heart disease?
# focus: bmi and sleeptime; does a person's bmi and hours of sleep impact the likelihood of developing heart disease?
def getCorrelative(df, x, y):
  set = df[["BMI", "SleepTime"]].dropna()
  x = set["BMI"]
  y = set["SleepTime"]

  slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

  slop = round(slope, 2)
  intercept = round(intercept, 2)

  x = np.linspace(28, 40)
  y = x * slope + intercept

  # corralation between bmi, sleeptime, physicalhealth, etc.
  plt.figure(figsize=(12, 8))
  corr = df.corr()
  sns.heatmap(corr, annot=True)

  sns.set(style="darkgrid")
  sns.set(rc={'figure.figsize':(12,8)})
  
  # creating a figure composed of 3 matplotlib.Axes objects
  f, (ax_box1, ax_box2, ax_hist) = plt.subplots(3, sharex=True, gridspec_kw={"height_ratios": (.15, .15, .85)})
  colours = ['#4285f4', '#ea4335', '#fbbc05', '#34a853']
  # assigning a graph to each axis
  sns.boxplot(x=df[df['HeartDisease']=='Yes']["BMI"], ax=ax_box1, color="#ea4335")
  sns.histplot(df[df['HeartDisease']=='Yes'], x="BMI", ax=ax_hist, kde=True, color="#ea4335")

  sns.boxplot(x=df[df['HeartDisease']=='No']["BMI"], ax=ax_box2, color='#4285f4')
  sns.histplot(df[df['HeartDisease']=='No'], x="BMI", ax=ax_hist, kde=True, color='#4285f4')

  # Remove x axis name for the boxplots
  ax_box1.set(xlabel='')
  ax_box2.set(xlabel='')

  plt.legend(title='', loc=2, labels=['Heart Disease', 'No HeartDisease'],bbox_to_anchor=(1.02, 1), borderaxespad=0.)

  return slope, intercept

# calculate the rate of change, against a limit
def getPredictive(df, slope, intercept):
  max, min = getOutliers(df, "BMI")
  if slope > 0:
    return max
  elif slope < 0:
    return min
  else:
    return 0

def user_options():
  print("\n")
  print("This dataset explores the correlation between body mass index (BMI) and Heart Disease; as well as SleepTime (in hours based on a 24-hour schedule).")
  print("\t[0] Exit the program.")
  print("\t[1] Outliers: Get the high and low values of body mass indexes (BMI).")
  print("\t[2] Summary: Get the sum and average of body mass indexes (BMI).")
  print("\t[3] Correlative: Get the correlation between body mass index (BMI) and sleeptime (as well as other features).")
  print("\t[4] Predictive: Get the rate of change of the dataset.")
  print("\t[5] Display data scheme and general data analysis of Heart Disease Dataset.")
  
  option = input("Please choose a function to run (enter number): ")

  return option

def main():
    print("Hi! Welcome to lab 4!\n")
    print("\n\tRetrieving data...\n")

    df = pd.read_csv("lab04\heart_2020_cleaned.csv")
    # convert AgeCategory column into mean ages; convert from categorical to continuous data
    mean_age = {'55-59':57, '80 or older':80, '65-69':67,
                      '75-79':77,'40-44':42,'70-74':72,'60-64':62,
                      '50-54':52,'45-49':47,'18-24':21,'35-39':37,
                      '30-34':32,'25-29':27}
    df['AgeCategory'] = df['AgeCategory'].apply(lambda x: mean_age[x])
    df['AgeCategory'] = df['AgeCategory'].astype('float')
    slope, intercept = getCorrelative(df, "BMI", "SleepTime")

    user = input("Would you like to run a function? (y/n): ")
    while (user.lower() == "yes" or user.lower() == "y"):
      option = user_options()
      print()

      if (option.lower() == 'no' or option.lower() == 'n'):
        break

      try:
        option = int(option)
      except ValueError:
        print('Invalid option. Please try again.')

      if option == 1:
        max, min = getOutliers(df, "BMI")
        print(f"The maximum body mass index (BMI) is {max} kg/m² and the minimum body mass index (BMI) is {min} kg/m².")
      elif option == 2:
        sum, avg = getSummary(df, "BMI")
        print(f"The sum of all body mass indexes (BMI) is {sum} kg/m² and the average body mass index (BMI) is {avg} kg/m².")
      elif option == 3:
        if slope > 0:
          print("As an individual's body mass index (BMI) increases, the number of hours spent sleeping increases (Observe Figure 1).")
        elif slope < 0:
          print("As an individual's body mass index (BMI) increases, the number of hours spent sleeping decreases (Observe Figure 1).")
        else:
          print("As an individual's body mass index (BMI) increases, the number of hours spent sleeping reaches its limit (Observe Figure 1).")
        print("Regardless, as an individual's body mass index (BMI) increases, the more likely they are found to have Heart Disease (Observe Figure 2).")
        plt.show()
      elif option == 4:
        limit = getPredictive(df, slope, intercept)
        print(f"The rate of change of an individual's body mass index (BMI) with respect to the number of hours of sleep they get is roughly {slope} kg/m² per hour of sleep.")
      elif option == 5:
        dataAnalysis(df)
      elif option == 0:
        break

      user = input("\nWould you like to run another function? (y/n): ")
      print()

    print("\nThank you!")


if __name__=="__main__":
  main()
