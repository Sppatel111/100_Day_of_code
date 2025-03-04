#Udemy day32
import random
import smtplib
import datetime as dt
import pandas as pd
from pass2 import PASSWORD1,EMAIL

my_email = EMAIL
password = PASSWORD1
PLACE = "[Name]"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"D:/SNEHA1/100_Day_of_code/31_1_DAY_21/SMTP/birthday_wishes/letters/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        name1 = content.replace(PLACE, birthday_person["name"])
        print(name1)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday! \n\n{name1}")

