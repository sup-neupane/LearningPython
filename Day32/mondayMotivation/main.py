import smtplib
import datetime as dt
from dotenv import load_dotenv # type: ignore
import os
import random


load_dotenv()  

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()

print(weekday)

if weekday == 4:
    with open("quotes.txt","r") as quotes:
        lines = quotes.readlines()

    lines = [line.strip() for line in lines]

    quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection: 

        connection.starttls()
        connection.login(user=MY_EMAIL, password= PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs= "terobau12@yahoo.com", 
                            msg = f"Subject:Hello\n\n {quote}")




