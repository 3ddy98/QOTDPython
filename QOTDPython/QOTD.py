import random
import logging
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
list = ['eaponce.vanguard@gmail.com']
def qsender():
	for emails in list:
		fromaddr="eaponce.vanguard@gmail.com"
		toaddr= emails
		msg=MIMEMultipart()
		msg['From'] = fromaddr
		msg['To']= toaddr
		msg['Subject'] = "Quote of the Day"
	

		filename = "troll.png"	
		attachment = open("troll.png","rb")

		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= {}".format(filename))
	
		lines = open('Quotes.txt').read().splitlines()
		quote = random.choice(lines)
		msg.attach(part)
	
		body = "Someone somewhere once said...\n{}".format(quote)
		msg.attach(MIMEText(body, 'plain'))

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr,"Password")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()

#The scheduler starts here
sched = BlockingScheduler()

sched.add_job(qsender, 'cron', hour ='18', minute ='31')
logging.basicConfig()
sched.start()
