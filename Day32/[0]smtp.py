from dotenv import load_dotenv # type: ignore
import os
import smtplib

load_dotenv()  

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


with smtplib.SMTP("smtp.gmail.com", 587) as connection: 

    connection.starttls()
    connection.login(user=MY_EMAIL, password= PASSWORD)

    connection.sendmail(from_addr=MY_EMAIL, to_addrs= "terobau12@yahoo.com", msg = "Subject:Hello\n\n This is the body of the email.")



