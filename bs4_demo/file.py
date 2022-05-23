'''
HTML parsing example using a sample html file within the same project directory. Resource: https://youtu.be/XVv6mJpFOb0 
'''
from bs4 import BeautifulSoup # import beautifulsoup library

# 1. open file and read content from file using 'read' mode
with open('bs4_demo\home.html', 'r') as html_file: 
  content = html_file.read()
  # print(content) # prints html content (not formatted)
  # print('')

  # 2. create instance of beautifulsoup library
  soup = BeautifulSoup(content, 'lxml') # first argument is content variable, second argument is for parser method
  print(soup.prettify()) # prints html content (formatted/readable)
  print('')

  # 3. find and find_all methods
  tags = soup.find('h5') # finds first element matching the tag
  print(tags)
  print('')
  courses_html_tags = soup.find_all('h5') # finds all elements matching the tag
  print(courses_html_tags) # prints as list
  print('')
  print("Course Offerrings:")
  for course in courses_html_tags:
    print(course.text) # prints only the text of previous list
  print('')

  # 4. apply find methods to scrape a web page to grab specific information (could use web browser inspect tool)
  # Goal: find and extract info on course and course prices
  course_cards = soup.find_all('div', class_ = 'card')
  for course in course_cards:
    course_name = course.h5.text
    course_price = course.a.text.split()[-1] # split method to access last element (just the price)

    # print(course_name)
    # print(course_price)

    print(f'{course_name} costs {course_price}') # formatted sentence
