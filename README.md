# Python Data Science
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Table of Contents
+ [Purpose](https://github.com/mcmunchie/python-data-science#purpose)
+ [Coding Environment](https://github.com/mcmunchie/python-data-science#coding-environment)
+ [Lab 01: Python Review](https://github.com/mcmunchie/python-data-science#lab-01-python-review)
+ [Lab 02: CDC CSV Data Analysis](https://github.com/mcmunchie/python-data-science#lab-02-cdc-csv-data-analysis)
+ [Lab 03: Data Processing and Mining using Pandas](https://github.com/mcmunchie/python-data-science#lab-03-data-processing-and-mining-using-pandas)
+ [Lab 04: Indicators of Heart Disease and Data Analysis](https://github.com/mcmunchie/python-data-science#lab-04-indicators-of-heart-disease-and-data-analysis)
+ [bs4: Simple Web Scraper](https://github.com/mcmunchie/python-data-science#bs4-simple-web-scraper)
+ [Reinforcement Learning: Q-Learning Algorithm](https://github.com/mcmunchie/python-data-science#reinforcement-learning-q-learning-algorithm)

## Purpose
Introduction to the data mining process and its application to real-world problems. Explored data preparation techniques, post-processing metrics to identify information of interest, supervised and unsupervised machine learning algorithms.

## Coding Environment
Python environment setup:
+ [VMware Workstation Player 16](https://www.vmware.com/products/workstation-player.html) running [Ubuntu](https://ubuntu.com/)
+ [JetBrains PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=windows)

Alternative Python environment setup:
+ [Visual Studio Code](https://code.visualstudio.com/download)

## Lab 01: Python Review
Review of basic Python functionality and programming.

## Lab 02: CDC CSV Data Analysis
Demonstrates data manipulation using a CSV file[^1] from the [CDC database](https://covid.cdc.gov/covid-data-tracker/#trends_dailycases). 

## Lab 03: Data Processing and Mining using Pandas
Demonstrates data analysis using Pandas library and CDC COVID-19 data through an API call. It takes awhile to retrieve the data from the CDC database at the start of the program.

## Lab 04: Indicators of Heart Disease and Data Analysis
Explores key indicators of Heart Disease using the following dataset from the [2020 Annual CDC survey data of 400k adults](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease?resource=download).

## bs4: Simple Web Scraper
Quick demo of the bs4 Python library used for parsing HTML and XML documents.

Installation:
+ run command to install bs4

  ``` terminal
  pip install beautifulsoup4
  ```
+ run command to install parser of choice

  ``` terminal
  pip install lxml
  pip install html5lib
  ```
+ run command to install requests library (used to exchange HTTP requests on the web)

  ``` terminal
  pip install requests
  ```

## Reinforcement Learning: Q-Learning Algorithm
Implementation of the Q-Learning algorithm by [Dr. Daniel Soper](https://youtu.be/iKdlKYG78j4). I recommend exploring Dr. Soper's [Artificial Intelligence Lessons](https://youtube.com/playlist?list=PL1LIXLIF50uWNLUnQRb3xLlsErSLLXryE) to learn more about reinforcement learning and the Q-Learning algorithm.

[^1]: Visit CDC database via the link above, scroll down to the 'Data Downloads and Footnotes' section, click the **plus** icon to expand the 'Data Table for Daily Case Trends - The United States' column, then click the big **Download Data** button. Now you've downloaded the *data_table_for_daily_case_trends__the_united_states* CSV file used in this lab.
