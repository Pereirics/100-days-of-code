import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "happybirthdaybot4@gmail.com"
PASSWORD = "omhyrtykmqkyqdot"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 0:
    with open("quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
        quote = choice(quotes)

    subj = "Monday Motivation"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="carinarita2002@gmail.com",
            msg=f"Subject:{subj}\n\n{quote}"
        )

