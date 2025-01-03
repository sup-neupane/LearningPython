import pandas as pd
import datetime as dt
import smtplib
from dotenv import load_dotenv # type: ignore
import os
import random


load_dotenv()  

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


#Getting todays date:
now = dt.datetime.now()
today = (now.month,now.day)

#Reading from CSV
df = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day) :data_row for (index, data_row) in df.iterrows()}

#Check for birthday:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

  
    with smtplib.SMTP("smtp.gmail.com", 587) as connection: 

        connection.starttls()
        connection.login(user=MY_EMAIL, password= PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )



