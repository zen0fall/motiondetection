# Sending sms in combination
# with Motion surveillance software
#
"""
Created on Thu Mar 29 20:00:33 2018

@author:zenofall
"""

import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


fromaddr = 'yourmail@gmail.com' #email from which this mail will be sent login below
toaddrs = 'anymail@anything.com','1xxxxxxxxxx.1xxxxxxxxxx.WvS-mS5WHd@txt.voice.google.com'  # can be list of strings (the x's are numbers from your google voice text to your mailbox)
#I typically just mail myself, so to address's can be you or your spouse 

username = fromaddr #enter your email to login, same as your fromaddr
password = 'password' #password for the above email
subject = 'Motion Detected'

#
# Email object
# 

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ",".join(toaddrs)
msg['Subject'] = subject

#
# Email body
#
body = 'A motion has been detected.\nTime: %s' % str(datetime.now())
msg.attach(MIMEText(body, 'plain'))

#
# Connecting to SMTP server and
# sending the email
#
smtp = smtplib.SMTP('smtp.gmail.com',587,timeout=120)
smtp.set_debuglevel(1)
smtp.connect('smtp.gmail.com', '587')
smtp.ehlo()
smtp.starttls()


smtp.login(username, password)
text = msg.as_string()
smtp.sendmail(fromaddr, toaddrs, text)
smtp.quit()


#
# Output
#
