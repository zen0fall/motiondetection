#author:zenofall

import argparse
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.encoders as Encoders

fromaddr = 'yourmail@gmail.com' #mail from , your mail address
toaddrs  = 'anymail@anything.com'  # can be list of strings
#I typically just mail myself, so to address's can be you or your spouse 

#Login for fromaddr email 
username = fromaddr #enter your email to login, same as your fromaddr
password = 'password' #password for the above email

subject = 'Video Recorded!'

#
# Email object
# 
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddrs
msg['Subject'] = subject


#
# Email attachement
#
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input file')
args = parser.parse_args()

part = MIMEBase('application', "octet-stream")
part.set_payload(open(args.input_file, "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition',
                'attachment; filename="%s"' % args.input_file)

msg.attach(part)

#
# Email body
#
body = 'This movie has been captured due to a motion which was just detected.'
body += '\nTime: %s' % str(datetime.now())
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
#print ("Message length is " + repr(len(msg)))
#print (text)
