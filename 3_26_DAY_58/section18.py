import smtplib
import getpass
import imaplib
import email

#put in config file.
EMAIL = "abcd1234567sp@gmail.com"
PASSWORD = "unjggoojpipszyqr"

# obj = smtplib.SMTP('smtp.gmail.com', 587)
# print(obj.ehlo())

# obj.starttls()
# obj.login(EMAIL,PASSWORD)

# obj.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f'Subject:Section 18\n\n about the email.')

# password = getpass.getpass('Password pls:')
#
# print(password)


## starting imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login(EMAIL, PASSWORD)
# print(M.list())

inb = M.select('inbox')
# print(inb)

# type,data=M.search(None,'BEFORE 26-Mar-2025')

# type,data=M.search(None,'FROM abcd1234567sp@gmail.com')

type, data = M.search(None, 'SUBJECT "Section 18"')

# print(type, data)

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
# print(email_data)

raw_email = email_data[0][1]
# print(raw_email)
raw_email_string=raw_email.decode('utf-8')
# print(raw_email_string)


## using email module for getting body part
email_message=email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() =='text/plain':
        body=part.get_payload(decode=True)
        print(body)