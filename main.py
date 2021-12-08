##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import smtplib
import datetime as dt
import os
import random

MY_EMAIL="jigyasa.sointernship@gmail.com"
MY_PASS="JIGYASA1216"

data=pandas.read_csv("birthdays.csv")
now=dt.datetime.now()
day=now.day
month=now.month


for index,row in data.iterrows():
    if row["month"]==month and row["day"]==day:
        # selecting random file
        dir="letter_templates"
        random_file=random.choice(os.listdir("/home/practicalmetal/Documents/Projects/Birthday Wisher/letter_templates"))
        path = os.path.join(dir, random_file)
        with open(path) as file:
            data=file.read()
            data=data.replace("[NAME]",row["name"])
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=row["email"],msg=f"Subject: Happy birthday!!\n\n{data}")


         



