import smtplib
import random
import pandas
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv('birthdays.csv')
print(data)
