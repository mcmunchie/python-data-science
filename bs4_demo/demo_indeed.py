'''
Uses requests library to find info on job postings.
'''
from bs4 import BeautifulSoup
import requests

# make a request using get method to access website's html
# text extentsion used to access text only
html_text = requests.get('https://www.indeed.com/jobs?q=software%20engineer&l=united%20states&vjk=f658335f1e70f71c').text
soup = BeautifulSoup(html_text, 'lxml')
# 1. find jobs (use web browser inspect tools)
jobs = soup.find_all('div', class_ = 'slider_container')
# for each job, find publish date, company name, job title, and job description
for job in jobs:
  published_date = job.find('span', class_ = 'date').text
  if '5' or '12' in published_date: # specified range of when job was posted
    company_name = job.find('span', class_ = 'companyName').text.replace(' ', '') # replace extra spaces with nothing (optional)
    job_title = job.find('h2', class_ = 'jobTitle').text
    skills = job.find('div', class_ = 'job-snippet').text

    # 2. print info
    print(f'''
    Company Name: {company_name}
    Job Title: {job_title}
    Job Description: {skills}
    ''')

    print('')
    