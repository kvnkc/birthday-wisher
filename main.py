import smtplib
import random
import pandas
import datetime as dt

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace('[NAME]', birthday_person['name'])
        print(birthday_person)

# my_email = "from@example.com"
# with smtplib.SMTP(host="smtp.mailtrap.io", port=2525) as connection:
#     connection.starttls()
#     connection.login(user='2a34c59a769644', password='18e850b3615af5')
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='Kevin.Cheung.Kai@gmail.com',
#                         msg='Subject: Hello\n\nThis is the body of my email'
#                         )
