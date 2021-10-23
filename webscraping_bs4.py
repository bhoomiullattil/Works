import requests  # http requests

from bs4 import BeautifulSoup  # web scraping
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placeholder

content = ''


# extracting Hacker News Stories


def extract_news(url):
    print('Extracting NDTV News Stories...')
    cnt = ''
    cnt += ('<b>Top Stories:</b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('h2', attrs={'class': 'newsHdng', 'valign': ''})):
        cnt += ((str(i + 1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        # print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
    return (cnt)
cnt=extract_news(input("enter url"))
#cnt=extract_news('https://www.ndtv.com/latest')
##cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')
content+=('<br>')
dta=input("enter comment")
content+=dta
# lets send the email

print('Composing Email...')

# update your email details
# make sure to update the Google Low App Access settings before

SERVER = 'smtp.gmail.com'  # "your smtp server"
PORT = 587  # your port number
FROM = 'xyz'  # "your from email id"
TO = 'xyz'  # "your to email ids"  # can be a list
PASS = 'xyz'  # "your email id's password"

# fp = open(file_name, 'rb')
# Create a text/plain message
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top News Stories NDTV[Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
    now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
#msg.attach(MIMEText(dta))
# fp.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.set_debuglevel(0)
server.ehlo()
server.starttls()
# server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()
