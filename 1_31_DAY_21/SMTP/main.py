#udemy day32
import smtplib
import datetime as dt
import random
from pass1 import PASSWORD,EMAIL

my_email = EMAIL
password = PASSWORD

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

if weekday == 4:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,msg=f"Subject:Friday Quotes \n\n {quote}")
else:
    print("hi")


