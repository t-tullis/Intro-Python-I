"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

user_input_year = input("Please enter a year(YYYY): ")
user_input_month = input("Please enter a month(ie: may = 5): ")

if not user_input_year and not user_input_month:
  now = datetime.now()
  print(calendar.month(now.year, now.month, w=0, l=0))
elif not user_input_year and user_input_month:
  now = datetime.now()
  if(int(user_input_month) < 1 or int(user_input_month) > 12):
    print("That is an invalid month. \nPlease enter a valid month")
  else:
    print(calendar.month(now.year, int(user_input_month), w=0, l=0))
elif user_input_year and user_input_month:
  print(calendar.month(int(user_input_year), int(user_input_month), w=0, l=0))
else:
  print("Please enter a valid year and month(1-12) in the proper format (YYYY/MM)")







